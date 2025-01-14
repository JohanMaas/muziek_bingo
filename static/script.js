    const albumContainer = document.getElementById("album-container");
        const songGrid = document.getElementById("song-grid");
        const songInfo = document.getElementById("song-info");
        const randomButton = document.getElementById("random-button");
        const resetButton = document.getElementById("reset-button");
        const carouselFrame = document.getElementById("carousel-frame");
        const rouletteSound = document.getElementById("roulette-sound");
        const f1keysound = document.getElementById("f1-key-sound");
        const f2keysound = document.getElementById("f2-key-sound");

        const albumImageCache = {};
        const placeholderCache = {};

        let availableSongs = [];
        let selectedSong = null;
        let animating = false;  // Prevents multiple simultaneous animations
        let lastSelectedIndex = 0;
        let availableSongsCache = [];

        function addSongToGrid(songTitle) {
            const cells = songGrid.getElementsByClassName("grid-item");
            for (const cell of cells) {
                if (cell.textContent.trim() === "") {
                    cell.classList.add('is-filled');
                    cell.textContent = songTitle;
                    break;
                }
            }
        }

        function resetGrid() {
            const cells = songGrid.getElementsByClassName("grid-item");
            for (const cell of cells) {
                cell.textContent = "";
            }
        }

        // Function to update the carousel image
        function updateWidgetImage(img, song) {
            const imgSrcKey = `/static/albums/${song.image}`;

            // Check if the album image is already cached
            if (albumImageCache[imgSrcKey]) {
                // Use the cached image if available
                img.src = albumImageCache[imgSrcKey];
            } else {
                // Load the image if not cached
                const image = new Image();
                image.src = imgSrcKey;

                image.onload = () => {
                    // Cache the image once loaded
                    albumImageCache[imgSrcKey] = image.src;
                    img.src = image.src;
                };

                image.onerror = () => {
                    // If the image fails to load, use the placeholder
                    img.src = createPlaceholderImage(song.title, 100, 10);
                };
            }
        }

        // Function to update the carousel with available songs
        async function updateCarousel() {
            await fetch("/available_songs")
                .then((response) => response.json())
                .then((availableSongs) => {
                    carouselFrame.innerHTML = ""; // Clear any existing content

                    // Calculate the number of widgets based on the screen size
                    const carouselWidth = window.outerWidth;
                    //console.log("carouselWidth: ", carouselFrame.clientWidth); // Debugging
                    const widgetWidth = 170; // Adjust this value based on your widget width
                    const numWidgets = Math.floor(carouselWidth / widgetWidth);

                    //const numWidgets = 15 ||availableSongs.length; // Fixed number of widgets
                    const middleIndex = Math.floor(numWidgets / 2); // Middle widget index

                    console.log("middleIndex: ", middleIndex); // Debugging
                    for (let i = 0; i < numWidgets; i++) {
                        const item = document.createElement("div");
                        item.classList.add("carousel-item");

                        if (i === middleIndex) {
                            item.classList.add("highlight-yellow"); // Highlight the middle widget
                        }

                        const img = document.createElement("img");
                        const songIndex = (availableSongs.length + i - middleIndex) % availableSongs.length; // Circular indexing
                        const albumImageUrl = `/static/albums/${availableSongs[songIndex].image}`;

                        img.onerror = () => {
                            img.src = createPlaceholderImage(
                                availableSongs[songIndex].title,
                                100,
                                10
                            );
                        };
                        img.src = albumImageUrl;
                        img.alt = availableSongs[songIndex].title;

                        const title = document.createElement("p");
                        title.textContent = availableSongs[songIndex].title;

                        item.appendChild(img);
                        item.appendChild(title);
                        carouselFrame.appendChild(item);
                    }

                    availableSongsCache = availableSongs; // Cache for animation
                })
                .catch((error) => console.error("Error fetching available songs:", error));
        }

        // Function to animate the carousel
        async function animateCarousel(direction, selectedIndex, onComplete) {
            if (animating) return; // Prevent overlapping animations
            animating = true;

            // Calculate the number of widgets based on the screen size
            const carouselWidth = window.outerWidth;
            //console.log("carouselWidth: ", carouselFrame.clientWidth); // Debugging
            const widgetWidth = 170; // Adjust this value based on your widget width
            const numWidgets = Math.floor(carouselWidth / widgetWidth);

//            const numWidgets = 15 || availableSongsCache.length; // Fixed number of visible widgets
            const middleIndex = Math.floor(numWidgets / 2); // Middle widget index
            const totalSongs = availableSongsCache.length;

            const carouselWidgets = carouselFrame.querySelectorAll(".carousel-item");
            if (!carouselWidgets.length) {
                animating = false;
                onComplete();
                return;
            }

            let currentMiddleIndex = parseInt(carouselWidgets[middleIndex].dataset.songIndex, 10) || 0;

            const startTime = performance.now();
            const animationDuration = 5000; // Total animation duration (5 seconds)
            const constantSpeedDuration = 3000; // Constant speed for first 3 seconds
            const slowingDownDuration = animationDuration - constantSpeedDuration;

            const updateContent = () => {
                const elapsedTime = performance.now() - startTime;
                const distanceToTarget = Math.abs((selectedIndex - currentMiddleIndex + totalSongs) % totalSongs);

                let step = 1; // Default step size (constant)

                if (elapsedTime >= constantSpeedDuration) {
                    // Slow down after 3 seconds
                    const timeLeft = animationDuration - elapsedTime;
                    const slowDownFactor = Math.max(timeLeft / slowingDownDuration, 0.1); // Minimum slowdown factor
                    step = Math.ceil(distanceToTarget * slowDownFactor);
                }

                // Update the middle widget
                currentMiddleIndex = (currentMiddleIndex + direction + totalSongs) % totalSongs;

                // Update widgets
                carouselWidgets.forEach((widget, index) => {
                    const songIndex = (currentMiddleIndex + index - middleIndex + totalSongs) % totalSongs;
                    const song = availableSongsCache[songIndex];

                    const img = widget.querySelector("img");

                    // Update the image for this widget
                    updateWidgetImage(img, song);

                    const title = widget.querySelector("p");
                    title.textContent = song.title;

                    widget.dataset.songIndex = songIndex;

                    // Highlight the middle widget
                    if (index === middleIndex) {
                        if (songIndex === selectedIndex) {
                            widget.classList.add("highlight-green");
                            widget.classList.remove("highlight-yellow");
                        } else {
                            widget.classList.add("highlight-yellow");
                            widget.classList.remove("highlight-green");
                        }
                    } else {
                        widget.classList.remove("highlight-yellow", "highlight-green");
                    }
                });

                // Ensure that animation continues until the content is correctly set
                if (carouselWidgets[middleIndex].dataset.songIndex == selectedIndex) {
                    animating = false;
                    onComplete();
                    scrollToMiddle(carouselFrame);
                    return;
                }

                // Continue the animation
                setTimeout(updateContent, 50); // Update widgets in intervals
                scrollToMiddle(carouselFrame);
            };

            updateContent();
            scrollToMiddle(carouselFrame);

        }




        function createPlaceholderImage(text, sizeEllipse, sizeFont) {
            const cacheKey = `${text}-${sizeEllipse}x${sizeFont}`;
            // If the image is already cached, return it
            if (placeholderCache[cacheKey]) {
                return placeholderCache[cacheKey];
            }

            const canvas = document.createElement("canvas");
            canvas.width = sizeEllipse;
            canvas.height = sizeEllipse;
            const ctx = canvas.getContext("2d");

            // Calculate usable radius (accounting for border)
            const borderThickness = 10;
            const radius = (sizeEllipse - borderThickness) / 2;
            const maxWidth = radius * 1.4; // 70% of diameter for safe text area

            // Draw circle
            ctx.beginPath();
            ctx.arc(sizeEllipse / 2, sizeEllipse / 2, radius, 0, 2 * Math.PI);

            // Fill and stroke
            ctx.fillStyle = "white";
            ctx.fill();
            ctx.lineWidth = borderThickness;
            ctx.strokeStyle = "black";
            ctx.stroke();

            // Text rendering
            let words = text.split(' ');
            let lines = [];
            let currentLine = words[0];

            // Set initial font
            ctx.font = `${sizeFont}px sans-serif`;
            ctx.fillStyle = "black";
            ctx.textAlign = "center";

            // Create word-wrapped lines
            for (let i = 1; i < words.length; i++) {
                let testLine = currentLine + ' ' + words[i];
                let metrics = ctx.measureText(testLine);
                if (metrics.width > maxWidth) {
                    lines.push(currentLine);
                    currentLine = words[i];
                } else {
                    currentLine = testLine;
                }
            }
            lines.push(currentLine);

            // Calculate vertical positioning
            const lineHeight = sizeFont * 1.2;
            const totalHeight = lineHeight * lines.length;
            let startY = (sizeEllipse - totalHeight) / 2 + lineHeight;

            // Draw lines
            lines.forEach((line, i) => {
                ctx.fillText(line, sizeEllipse / 2, startY + (i * lineHeight));
            });

            // Cache the generated placeholder image
            const dataUrl = canvas.toDataURL();
            placeholderCache[cacheKey] = dataUrl;
            return dataUrl;
        }

        // Function to initialize the album container with a placeholder
        function initializePlaceholder() {
            const albumContainer = document.getElementById("album-container");
            const songInfo = document.getElementById("song-info");

//            const placeholderImage = createPlaceholderImage("Nog geen nummer getrokken", 200, 12);

            // Set the placeholder image and text
            albumContainer.innerHTML = `<img src="${placeholderImage}" alt="Placeholder">`;
            songInfo.innerHTML = "<h2>Nog geen nummer getrokken</h2>";
        }

        let currentAudio = null; // Keep track of the currently playing audio

        async function playPreview(trackId) {
            const apiUrl = `http://127.0.0.1:5000/api/spotify-preview/${trackId}`;
            
            try {
                // Stop the currently playing audio (if any)
                if (currentAudio) {
                    currentAudio.pause();
                    currentAudio = null; // Clear the reference
                }
        
                const response = await fetch(apiUrl);
                if (!response.ok) {
                    throw new Error(`Failed to fetch preview URL: ${response.statusText}`);
                }
        
                const data = await response.json();
                const previewUrl = data.preview_url;
        
                if (previewUrl) {
                    console.log("Playing preview URL:", previewUrl); // Log the preview URL
                    currentAudio = new Audio(previewUrl);
                    currentAudio.play().catch((error) => console.error("Error playing preview:", error));
                } else {
                    console.error("Preview URL not available for this track.");
                }
            } catch (error) {
                console.error("Error fetching preview URL:", error);
            }
        }
        
    
        // Handle random button click
        randomButton.addEventListener("click", async() => {
            const svgContainer = document.getElementById('bingo-winner-animation');
            svgContainer.style.display = 'none'; // Hide the SVG animation

            let selectedIndex = 0
            randomButton.disabled = true; // Disable the button during the animation
            await updateCarousel();
            await fetch("/random_song", { method: "POST" })
                .then(response => response.json())
                .then(data => {
                    if (data.status === "success") {
                        const song = data.song;


                        selectedSong = song;  // Store the selected song

                        console.log("Available songs:", data.available_songs);  // Debugging
                        availableSongs = data.available_songs;  // Update available songs from the backend response
                        selectedIndex = availableSongs.findIndex(s => s.title === selectedSong.title);
                        console.log("Selected song:", selectedSong.title);
                        console.log("Selected index:", selectedIndex);
                        // Start the highlight animation
                         availableSongs = data.available_songs;
                    } else {
                        albumContainer.innerHTML = `<p>${data.message}</p>`;
                    }
                });

                   let song = availableSongs[selectedIndex]
                   rouletteSound.play(); // Play the roulette sound effect
                   animateCarousel(1, selectedIndex, () => {
                            rouletteSound.pause(); // Stop the sound effect
                            // Once animation is complete, show the album cover
                            const albumImageUrl = `/static/albums/${song.image}`;
                            const image = new Image();
                            image.onload = () => {
                                albumContainer.innerHTML = `<img class="rotating" src="${albumImageUrl}" alt="${song.title}">`;
                            };
                            image.onerror = () => {
                                // Generate placeholder image if the album image is missing
                                const placeholderImage = createPlaceholderImage(song.title, 200, 20);
                                albumContainer.innerHTML = `<img class="rotating" src="${placeholderImage}" alt="${song.title}">`;
                            };

                            // Try to load the album image
                            image.src = albumImageUrl;

                            songInfo.innerHTML = `<h1>${song.artist} - ${song.title}</h1>`;
                            addSongToGrid(`${song.title}`);
                            console.log("Selected song track: ", song.track_id);
                            playPreview(song.track_id);

                            randomButton.disabled = false; // Re-enable the button
                        });

        });

        // Handle reset button click
        resetButton.addEventListener("click", () => {
        if (window.confirm('Weet je zeker dat je de bingokaart wilt resetten?')) {
         fetch("/reset", { method: "POST" })
                .then(response => response.json())
                .then(data => {
                    if (data.status === "success") {
                        // Stop the currently playing audio (if any)
                        if (currentAudio) {
                            currentAudio.pause();
                            currentAudio = null;
                        }
                        // Reset the UI
                        alert(data.message);
                        albumContainer.innerHTML = `<p></p>`;
                        songInfo.innerHTML = `<h2>Getrokken nummers:</h2>`;
                        resetGrid();
                        // Update the carousel with available songs
                        updateCarousel();
                    } else {
                        alert("Failed to reset songs.");
                    }
                });
        }

        });

        // Add event listener for F1 key press to play the sound
        document.addEventListener("keydown", (event) => {
            if (event.key === "F1") {
                event.preventDefault(); // Prevent the default action of the F1 key

                // Stop any currently playing Spotify album MP3
                if (currentAudio && !currentAudio.paused) {
                    currentAudio.pause();
                    currentAudio.currentTime = 0; // Reset the audio to the beginning
                }

                if (f1keysound.paused) {
                    f1keysound.loop = true; // Enable looping
                    f1keysound.play(); // Play the F1 sound effect
                } else {
                    f1keysound.loop = false; // Disable looping
                    f1keysound.pause(); // Pause the sound effect
                    f1keysound.currentTime = 0; // Reset the sound to the beginning
                }
            }
        });       

        // Add event listener for F2 key press to play the sound
        document.addEventListener("keydown", (event) => {
            if (event.key === "F2") {
                event.preventDefault(); // Prevent the default action of the F1 key

                // Stop any currently playing Spotify album MP3
                if (currentAudio && !currentAudio.paused) {
                    currentAudio.pause();
                    currentAudio.currentTime = 0; // Reset the audio to the beginning
                }

                if (f2keysound.paused) {
                    f2keysound.loop = true; // Enable looping
                    f2keysound.play(); // Play the F1 sound effect
                } else {
                    f2keysound.loop = false; // Disable looping
                    f2keysound.pause(); // Pause the sound effect
                    f2keysound.currentTime = 0; // Reset the sound to the beginning
                }
            }
        });             

        document.addEventListener('keydown', function(event) {
            if (event.key === 'F4') {
                event.preventDefault(); // Prevent the default action of the F4 key                
                const svgContainer = document.getElementById('bingo-winner-animation');
                if (svgContainer.style.display === 'block') {
                    svgContainer.style.display = 'none';
                } else {
                    svgContainer.style.display = 'block';
                }
            }
        });

        // Initialize grid based on the total number of songs
        function initializeGrid(numSongs) {
            songGrid.innerHTML = ""; // Clear any existing grid items
            for (let i = 0; i < numSongs; i++) {
                const div = document.createElement("div");
                div.className = "grid-item";
                songGrid.appendChild(div);
            }
        }

        // Call this function after fetching the available songs
        async function fetchAvailableSongs() {
            const response = await fetch("/available_songs");
            const data = await response.json();
            availableSongs = data;
            initializeGrid(availableSongs.length); // Initialize grid based on the number of songs
//            updateSongGrid();
        }

        // Call the function to initialize the placeholder when the app starts
        document.addEventListener("DOMContentLoaded", () => {
//            initializePlaceholder();
        });

        // Initial call to populate the song grid
        fetchAvailableSongs();

        // Update the carousel with available songs
        updateCarousel();

 const scrollToMiddle = (el) => {
        const middlePosition = el.parentNode.scrollWidth / 2 - el.parentNode.clientWidth / 2;
        el.parentNode.scrollLeft = middlePosition;

    };

// const carouselFrameEl = document.getElementById("carousel-frame");
 //scrollToMiddle(carouselFrame);

