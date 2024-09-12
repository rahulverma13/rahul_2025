---
layout: page
title: About
permalink: /about/
---

<!-- SASS Styles -->
<style lang="scss">
// Variables
$primary-color: #3498db;
$secondary-color: #00A36C;
$link-color: #9b59b6;
$border-radius: 8px;

// Mixins
@mixin flex-container {
  display: flex;
  align-items: flex-start;
}

@mixin image-style {
  width: 100%;
  border-radius: $border-radius;
}

// Global Styles
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
}

// Page Title
.page-title {
  color: $primary-color;
}

// Section Styles
.section-title {
  color: $secondary-color;
}

// Content Block
.content-block {
  @include flex-container;
  margin-bottom: 20px;

  .image-container {
    flex: 0 0 150px;
    margin-right: 20px;

    img {
      @include image-style;
    }
  }

  .text-container {
    flex: 1;

    h3 {
      margin-top: 0;
    }

    a {
      color: $link-color;
      text-decoration: none;

      &:hover {
        text-decoration: underline;
      }
    }
  }
}

// Contact Section
.contact-section {
  margin-top: 30px;

  h2 {
    color: $secondary-color;
  }
}

// Utterances script container
.utterances {
  margin-top: 40px;
}
</style>

<!-- HTML Structure -->
<h1 class="page-title">All about Rahul Verma</h1>

<p>Welcome to my AP CSA website! Here's a little about myself:</p>

<h2 class="section-title">Interests and Activities</h2>

<div class="content-block">
  <div class="image-container">
    <img src="https://github.com/user-attachments/assets/58bcc164-06b4-4494-94c4-5a06c0c1f8c8" alt="Competitive Programming">
  </div>
  <div class="text-container">
    <h3>Competitive Programming</h3>
    <p>I really enjoy programming problem solving in competitions like <a href="https://usaco.org">USACO</a> and <a href="https://www.acsl.org">ACSL</a>. I've been doing this for a few years and have really enjoyed learning this side of coding.</p>
  </div>
</div>

<div class="content-block">
  <div class="image-container">
    <img src="../images/Robot2.png" alt="Robotics">
  </div>
  <div class="text-container">
    <h3>Robotics</h3>
    <p>As a co-captain of my <a href="https://www.firstinspires.org/robotics/ftc">FTC</a> team, I take on a lot of responsibilities on the hardware side, and I also contribute to the programming. This past summer, we designed and built a suspension coaxial swerve drive, which was an exciting and challenging project!</p>
  </div>
</div>

<div class="content-block">
  <div class="image-container">
    <img src="../images/lakers.png" alt="Basketball">
  </div>
  <div class="text-container">
    <h3>Basketball</h3>
    <p>I love playing basketball and am looking forward to making the varsity team this year, after being on JV last year. My favorite team is the Los Angeles Lakers, and are hopeful they can get back to their 2020 form and win a championship.</p>
  </div>
</div>

<div class="contact-section">
  <h2>Contact</h2>
  <p>Feel free to reach out to me at connect.rahulv@gmail.com for anything!</p>
</div>

<script src="https://utteranc.es/client.js"
        repo="rahulverma13/rahul_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>