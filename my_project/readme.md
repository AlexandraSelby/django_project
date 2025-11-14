# Django Fragrance Review App

## Contents

* [Project Overview](#project-overview)
* [User Stories](#user-stories)
* [Technologies Used](#technologies-used)
* [Acknowledgments](#acknowledgments)
* [References](#references)
* [Installation and Access](#installation-and-access)
* [Deployment](#deployment)
* [Project Structure](#project-structure)

  * [Typography and Design System](#typography-and-design-system)
  * [Wireframes](#wireframes)
  * [Colour Palette & Accessibility Update](#colour-palette--accessibility-update)
* [Changes Summary](#changes-summary)
* [Testing and Validation](#testing-and-validation)

  * [Manual Functional Testing](#manual-functional-testing)
  * [Accessibility Testing (WAVE)](#accessibility-testing-wave)
  * [Keyboard Accessibility](#keyboard-accessibility)
  * [Backend API Testing](#backend-api-testing)
* [Version History and Commit Highlights](#version-history-and-commit-highlights)
* [Performance Considerations](#performance-considerations)
* [Limitations](#limitations)
* [Future Enhancements](#future-enhancements)
* [Real-Life Application & Project Continuity](#real-life-application--project-continuity)
* [Reflection](#reflection)
* [How to Use This Work](#how-to-use-this-work)
* [License](#license)

## Project Overview
# Django Fragrance Review App

## Contents

* [Project Overview](#project-overview)
* [User Stories](#user-stories)
* [Technologies Used](#technologies-used)
* [Acknowledgments](#acknowledgments)
* [References](#references)
* [Installation and Access](#installation-and-access)
* [Deployment](#deployment)
* [Project Structure](#project-structure)

  * [Typography and Design System](#typography-and-design-system)
  * [Wireframes](#wireframes)
  * [Colour Palette & Accessibility Update](#colour-palette--accessibility-update)
* [Changes Summary](#changes-summary)
* [Testing and Validation](#testing-and-validation)

  * [Manual Functional Testing](#manual-functional-testing)
  * [Accessibility Testing (WAVE)](#accessibility-testing-wave)
  * [Keyboard Accessibility](#keyboard-accessibility)
  * [Backend API Testing](#backend-api-testing)
* [Version History and Commit Highlights](#version-history-and-commit-highlights)
* [Performance Considerations](#performance-considerations)
* [Limitations](#limitations)
* [Future Enhancements](#future-enhancements)
* [Real-Life Application & Project Continuity](#real-life-application--project-continuity)
* [Reflection](#reflection)
* [How to Use This Work](#how-to-use-this-work)
* [License](#license)

## Project Overview

The Django Fragrance Review App is a web application designed to showcase fragrance reviews within a clean, organised, and scalable Django framework. Developed as part of my ongoing progress in the Code Institute Level 5 Diploma, this project builds upon the foundations laid in my previous work—particularly the **“What’s Your Scent Spirit?”** fragrance quiz, which has been fully integrated into this site through a dedicated link on the homepage.

This project is not a standalone exercise; it is part of a growing ecosystem. The fragrance quiz integrates personality-driven scent recommendations powered by AI, while this Django review app focuses on user-generated reviews and structured content. Together, they form the early stages of a larger vision I plan to expand in the next milestone project.

Looking ahead, I intend for this Django application to evolve into the backbone of a more complete fragrance platform. Future features may include fragrance product listings, membership functionality, user accounts, or curated scent collections. This aligns closely with my long-term goal of building a real, usable fragrance-focused web experience that goes beyond coursework.

Fragrance is a personal special interest of mine, and this app represents the practical beginning of a project I fully intend to use beyond graduation—merging technical development with a genuine passion.

## User Stories
## User Stories  

### User Story 1 – Explore Fragrance Reviews Easily  
**As a fragrance enthusiast, I want to browse a curated list of fragrance reviews so that I can discover new scents quickly and understand what others think of them.**  

**Acceptance Criteria**  
- A reviews page displays all available entries in a clean and consistent layout.  
- Each review includes a clear title, short snippet, or summary.  
- The page is responsive and easy to read across desktop and mobile.  

**Tasks**  
- Implement a Django view to query and return all reviews.  
- Create a template to display reviews in a structured, readable list.  
- Apply CSS styling to ensure visual clarity and consistency.  

---

### User Story 2 – View Full Review Details  
**As a curious user, I want to click on a review and read its full content so that I can explore a fragrance in more depth.**  

**Acceptance Criteria**  
- Each review has its own dedicated detail page.  
- The page displays the full review text, author, and timestamps.  
- URL structure is predictable (e.g., `/reviews/<id>/`).  

**Tasks**  
- Build a Django detail view that retrieves a review by ID.  
- Create a styled template for displaying full review content.  
- Add navigation links to move back to the reviews list.  

---

### User Story 3 – Edit Existing Reviews  
**As a reviewer or admin, I want to edit an existing fragrance review so that I can update information, refine descriptions, or correct mistakes.**  

**Acceptance Criteria**  
- Authenticated users see an **Edit** button on each review.  
- Editing opens a form pre-filled with the review’s current content.  
- Saving changes updates the review and redirects to the detail page.  

**Tasks**  
- Implement Django’s `UpdateView` for editing reviews.  
- Create an edit form template styled consistently with the rest of the site.  
- Add conditional logic to show the Edit button only to authenticated users.  

---

### User Story 4 – Delete Reviews When Needed  
**As a reviewer or admin, I want to delete a fragrance review so that I can remove outdated or incorrect content from the site.**  

**Acceptance Criteria**  
- Authenticated users see a **Delete** button on each review.  
- A confirmation page appears before the review is permanently removed.  
- Deleted reviews disappear from all lists and can no longer be accessed.  

**Tasks**  
- Configure Django’s `DeleteView` and confirmation template.  
- Add secure authentication checks before allowing deletion.  
- Update templates so Delete buttons appear only for authorised users.  

---

### User Story 5 – Navigate the Website and Integrated Quiz Smoothly  
**As a user, I want intuitive navigation so that I can move easily between the homepage, reviews, review details, and the integrated fragrance quiz experience.**  

**Acceptance Criteria**  
- Navigation links are visible within a shared base template.  
- The “Find Your Fragrance” quiz button links to the external quiz app.  
- All internal routes load cleanly with no broken links or template errors.  

**Tasks**  
- Implement a reusable `base.html` template with navigation links.  
- Add a clear CTA directing users to the integrated fragrance quiz.  
- Test navigation flow to ensure consistency and smooth transitions.  

## Technologies Used  

### Django  
Used as the main backend framework to structure the application, handle routing, manage models, and provide secure form processing through Django’s built-in class-based views.

### Python  
The core programming language powering the application logic, data handling, and server-side functionality.

### SQLite (Development Database)  
Used as the initial lightweight development database for local setup and early testing, before switching to a hosted database service for deployment.

### PostgreSQL (Heroku)  
Configured as the production database via Heroku’s managed PostgreSQL service. This allows the app to run on a more robust, scalable database engine with environment-based configuration rather than hardcoded credentials.

### HTML5 & Django Templates  
Used to structure all page layouts, extend base templates, and ensure clean, semantic markup throughout the site.

### CSS3  
Applied to style the interface, control layout spacing, and maintain consistency across the homepage, reviews list, and detail pages.

### Git & GitHub  
Used for version control, tracking changes, managing commits, and storing the project repository while keeping sensitive settings (such as the Django secret key and database credentials) out of version control.

### VS Code & GitHub Desktop  
Tools used during development for writing code, inspecting changes, committing updates, and managing the repository in a more visual way.

### Heroku  
Used as the hosting platform for deploying the Django project, managing environment variables, and connecting the app to a PostgreSQL database in a production-like environment.

### Canva  
Used to create and refine visual assets (such as hero images or supporting graphics) so that the site presentation aligns with the fragrance theme and feels cohesive with the existing quiz project branding.

### Fragrance Quiz Integration  
The previously built **“What’s Your Scent Spirit?”** quiz is integrated into this project through a dedicated CTA link, connecting both projects and forming the foundation of a future unified fragrance platform.

## Project Structure

django_project/
├── .venv/ # Virtual environment (not committed)
├── my_project/ # Main Django project folder
│ ├── pycache/
│ ├── init.py
│ ├── .env # Environment variables (secret key, DB config)
│ ├── .gitignore
│ ├── asgi.py
│ ├── readme.md
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── reviews/ # Core application for fragrance reviews
│ ├── pycache/
│ ├── migrations/ # Auto-generated database migrations
│ ├── static/ # App-specific static files
│ ├── templates/
│ │ └── reviews/ # All review-related HTML templates
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py # Forms for creating/editing reviews
│ ├── models.py # Review model definition
│ ├── test.py
│ ├── tests.py
│ ├── urls.py # App-level URL patterns
│ ├── views.py # Logic for list, detail, edit, delete views
│
├── .gitignore
├── db.sqlite3 # Local development database
├── manage.py
├── Procfile # Heroku process file
├── requirements.txt # Project dependencies
└── runtime.txt # Python runtime for Heroku

### Models

### Views

### Templates

### URLs

## Design System & Typography

## Wireframes

## Testing and Validation

### HTML/CSS Validation

### Python & Django Checks

### Manual Functional Testing

## Version History and Commit Highlights

## Deployment

## Future Enhancements

## Reflection


## Database Switch & Secret Key Security

## Features

## User Stories

## Technologies Used

## Project Structure

### Models

### Views

### Templates

### URLs

## Design System & Typography

## Wireframes

## Testing and Validation

### HTML/CSS Validation

### Python & Django Checks

### Manual Functional Testing

## Version History and Commit Highlights

## Deployment

## Future Enhancements

## Reflection
