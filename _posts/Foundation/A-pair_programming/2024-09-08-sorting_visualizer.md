---
layout: base
title: Sorting Algorithm Visualizer
description: Visualizes sorting algorithms
hide: false
---

<style>
    body {
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        text-align: center;
    }
    #inputSection, #visualizerSection {
        margin-bottom: 20px;
    }
    #numbers {
        width: 100%;
        height: 50px;
        margin-bottom: 10px;
    }
    select, button {
        margin: 5px;
        padding: 5px 10px;
    }
    #arrayContainer {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 20px;
    }
    .number-box {
        width: 40px;
        height: 40px;
        margin: 5px;
        background-color: #3498db;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    #stepCounter {
        font-size: 18px;
        margin-top: 10px;
    }
    #statusMessage {
        font-size: 18px;
        color: green;
        margin-top: 10px;
        display: none;
    }
</style>

<h1>Sorting Algorithm Visualizer</h1>

<div id="inputSection">
    <textarea id="numbers" placeholder="Enter numbers separated by commas (e.g., 5, 2, 8, 12, 1, 6)"></textarea>
    <br>
    <select id="algorithm">
        <option value="bubble">Bubble Sort</option>
        <option value="merge">Merge Sort</option>
        <option value="quick">Quick Sort</option>
    </select>
    <button onclick="startVisualization()">Start Visualization</button>
</div>

<div id="visualizerSection" style="display: none;">
    <div id="arrayContainer"></div>
    <div id="stepCounter">Step: 0</div>
    <button id="nextStepBtn" onclick="nextStep()">Next Step</button>
    <button onclick="resetVisualization()">Reset</button>
    <div id="statusMessage">Array is sorted!</div>
</div>

<script>
    let numbers = [];
    let algorithm = '';
    let currentStep = 0;
    let sortingSteps = [];
    let isSorted = false;

    function startVisualization() {
        const input = document.getElementById('numbers').value;
        numbers = input.split(',').map(num => parseInt(num.trim())).filter(num => !isNaN(num));
        algorithm = document.getElementById('algorithm').value;

        if (numbers.length === 0) {
            alert('Please enter valid numbers.');
            return;
        }

        document.getElementById('inputSection').style.display = 'none';
        document.getElementById('visualizerSection').style.display = 'block';

        initializeVisualization();
        generateSortingSteps();
        updateVisualization();
        updateStepCounter();
    }

    function initializeVisualization() {
        const container = document.getElementById('arrayContainer');
        container.innerHTML = '';

        numbers.forEach(num => {
            const box = document.createElement('div');
            box.className = 'number-box';
            box.textContent = num;
            container.appendChild(box);
        });
    }

    function generateSortingSteps() {
        sortingSteps = [numbers.slice()];
        let tempArray = numbers.slice();

        if (algorithm === 'bubble') {
            bubbleSort(tempArray);
        } else if (algorithm === 'merge') {
            mergeSort(tempArray, 0, tempArray.length - 1);
        } else if (algorithm === 'quick') {
            quickSort(tempArray, 0, tempArray.length - 1);
        }
    }

    function bubbleSort(arr) {
        const n = arr.length;
        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                    sortingSteps.push(arr.slice());
                }
            }
        }
    }

    function mergeSort(arr, left, right) {
        if (left >= right) {
            return;
        }
        const mid = left + Math.floor((right - left) / 2);
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }

    function merge(arr, left, mid, right) {
        const leftArr = arr.slice(left, mid + 1);
        const rightArr = arr.slice(mid + 1, right + 1);
        let i = 0, j = 0, k = left;

        while (i < leftArr.length && j < rightArr.length) {
            if (leftArr[i] <= rightArr[j]) {
                arr[k] = leftArr[i];
                i++;
            } else {
                arr[k] = rightArr[j];
                j++;
            }
            k++;
            sortingSteps.push(arr.slice());
        }

        while (i < leftArr.length) {
            arr[k] = leftArr[i];
            i++;
            k++;
            sortingSteps.push(arr.slice());
        }

        while (j < rightArr.length) {
            arr[k] = rightArr[j];
            j++;
            k++;
            sortingSteps.push(arr.slice());
        }
    }

    function quickSort(arr, low, high) {
        if (low < high) {
            const pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    function partition(arr, low, high) {
        const pivot = arr[high];
        let i = low - 1;

        for (let j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                [arr[i], arr[j]] = [arr[j], arr[i]];
                sortingSteps.push(arr.slice());
            }
        }

        [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
        sortingSteps.push(arr.slice());
        return i + 1;
    }

    function nextStep() {
        if (isSorted) {
            return;
        }

        if (currentStep < sortingSteps.length - 1) {
            currentStep++;
            updateVisualization();
            updateStepCounter();
        }

        // Check if sorting is complete
        if (currentStep === sortingSteps.length - 1) {
            if (isArraySorted(sortingSteps[currentStep])) {
                isSorted = true;
                document.getElementById('statusMessage').style.display = 'block';
            }
        }
    }

    function isArraySorted(arr) {
        for (let i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i - 1]) {
                return false;
            }
        }
        return true;
    }

    function updateVisualization() {
        const container = document.getElementById('arrayContainer');
        const boxes = container.getElementsByClassName('number-box');

        for (let i = 0; i < numbers.length; i++) {
            boxes[i].textContent = sortingSteps[currentStep][i];
            boxes[i].style.order = i;
        }
    }

    function updateStepCounter() {
        document.getElementById('stepCounter').textContent = `Step: ${currentStep}`;
    }

    function resetVisualization() {
        document.getElementById('inputSection').style.display = 'block';
        document.getElementById('visualizerSection').style.display = 'none';
        currentStep = 0;
        sortingSteps = [];
        isSorted = false;
        document.getElementById('statusMessage').style.display = 'none';
        updateStepCounter();
    }
</script>