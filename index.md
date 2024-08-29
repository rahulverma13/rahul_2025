---
layout: base
title: Student Home 
description: Home Page
hide: true
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rahul Verma's 2024-2025 AP CSA Notebook</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #333;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        .header {
            background: #333;
            color: #fff;
            padding: 30px 0;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 2em;
        }
        .intro {
            background: #fff;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .section {
            background: #fff;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .section h2 {
            color: #333;
        }
        .section img {
            float: right;
            margin-left: 20px;
            border-radius: 8px;
            width: 150px;
            height: auto;
        }
        .section p {
            line-height: 1.6;
        }
        .footer {
            background: #333;
            color: #fff;
            padding: 10px 0;
            text-align: center;
            position: relative;
            bottom: 0;
            width: 100%;
        }
        #game-container {
            background-color: #f0f0f0;
            border-radius: 8px;
            padding: 20px;
            margin-top: 20px;
            text-align: center;
        }
        #sentence-display {
            font-size: 18px;
            margin-bottom: 20px;
        }
        #user-input {
            width: 80%;
            padding: 10px;
            font-size: 16px;
        }
        #result {
            margin-top: 20px;
            font-weight: bold;
        }
        .correct {
            color: green;
        }
        .incorrect {
            color: red;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Welcome to Rahul Verma's 2024-2025 AP CSA Notebook!</h1>
    </div>

    <div class="container">
        <div class="intro">
            <p>Thank you for coming over to my website! Below I've listed some of my recent programming experiences that I'd like to highlight. If you want to learn more about me, head on over to my about me page.</p>
        </div>

        <div class="section">
            <h2>REHS</h2>
            <img src="./images/REHS.png" alt="REHS Image">
            <p>
                Over the summer, I completed a research internship at the San Diego Computer Center called the UCSD Research Experience for High School Students. In a project called ICICLE in which our subproject was named PRISM, we benchmarked the runtimes and efficiencies of the computer vision models Tensorflow and Pytorch against various CPU and GPU cores. These benchmarks lay the foundation for running CV models on fields in Iowa (the focus of the project) efficiently and quickly to assist with agriculture. We are looking forward towards continuing working on this project and submitting our paper/poster to research conferences.
            </p>
        </div>

        <div class="section">
            <h2>USACO/ACSL</h2>
            <img src="./images/USACO.png" alt="USACO/ACSL Image">
            <p>
                I have been preparing and competing in the USA Computing Olympiad (USACO) and American Computer Science League (ACSL) in recent years-- computer science competitions focused around problem solving and algorithms. I have qualified for USACO Silver (and nearly USACO Gold..) and won the ACSL Silver Medal in the national senior competition over recent years. With this, I have just recently become the president of the Del Norte Algorithmic Coding Club and hope to further the progress of algorithmic programming at our school.
            </p>
        </div>

        <div class="section">
            <h2>FTC Robotics</h2>
            <img src="./images/Robot1.png" alt="FTC Robotics Image">
            <p>
                As co-captain of my robotics team, we developed a complex drivetrain this summer (see my about me page for more). This requires a lot more programming, which I assisted my software team in completing (Tarun Jaikumar and Aadit Mathur played the biggest part in this 🙂). We are hopeful to qualify for the World Championships and win awards there too.
            </p>
        </div>

        <div id="game-container">
            <h2>Gorrila Type 😋</h2>
            <div id="sentence-display"></div>
            <input type="text" id="user-input" placeholder="Start typing here..." disabled>
            <div id="result"></div>
        </div>
    </div>

    <div class="footer">
        <p>&copy; 2024-2025 Rahul Verma. All rights reserved.</p>
    </div>

    <script>
        const sentenceDisplay = document.getElementById('sentence-display');
        const userInput = document.getElementById('user-input');
        const result = document.getElementById('result');
        
        let startTime, endTime;
        let currentSentence = '';
        let currentIndex = 0;
        let gameStarted = false;

        async function fetchRandomSentences() {
            try {
                const response = await fetch('https://api.quotable.io/quotes/random?limit=1');
                const data = await response.json();
                return data.map(quote => quote.content).join(' ');
            } catch (error) {
                console.error('Error fetching sentences:', error);
                return 'The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs. How vexingly quick daft zebras jump!';
            }
        }

        function updateDisplay() {
            let displayHTML = '';
            for (let i = 0; i < currentSentence.length; i++) {
                if (i < currentIndex) {
                    displayHTML += `<span class="correct">${currentSentence[i]}</span>`;
                } else if (i === currentIndex) {
                    displayHTML += `<span class="incorrect">${currentSentence[i]}</span>`;
                } else {
                    displayHTML += currentSentence[i];
                }
            }
            sentenceDisplay.innerHTML = displayHTML;
        }

        function startGame() {
            fetchRandomSentences().then(sentences => {
                currentSentence = sentences;
                currentIndex = 0;
                gameStarted = false;
                updateDisplay();
                userInput.value = '';
                userInput.disabled = false;
                userInput.focus();
                result.textContent = '';
            });
        }

        function endGame() {
            endTime = new Date();
            const timeElapsed = (endTime - startTime) / 1000; // in seconds
            const wordsTyped = currentSentence.split(' ').length;
            const wpm = Math.round((wordsTyped / timeElapsed) * 60);
            
            result.textContent = `Time: ${timeElapsed.toFixed(2)} seconds | Speed: ${wpm} WPM`;
            userInput.disabled = true;
            
            setTimeout(() => {
                if (confirm('Well done! Do you want to play again?')) {
                    startGame();
                }
            }, 100);
        }

        userInput.addEventListener('input', () => {
            const typedChar = userInput.value.slice(-1);
            if (typedChar === currentSentence[currentIndex]) {
                if (!gameStarted) {
                    startTime = new Date();
                    gameStarted = true;
                }
                currentIndex++;
                updateDisplay();
                if (currentIndex === currentSentence.length) {
                    endGame();
                }
            }
            userInput.value = userInput.value.slice(0, currentIndex);
        });

        // Start the game when the page loads
        startGame();
    </script>
</body>
</html>