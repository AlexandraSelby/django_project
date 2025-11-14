
## Project Overview
# Django Fragrance Review App

## Contents

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
  * [Colour Palette & Accessibility Update](#colour-palette--accessibility-update)
* [Database Configuration and Migration](#database-configuration-and-migration)
* [Testing and Validation](#testing-and-validation)
  * [HTML & CSS Validation](#html--css-validation)
  * [Python & Django Checks](#python--django-checks)
  * [Manual Functional Testing](#manual-functional-testing)
  * [Automated Testing: Review Access Control (TDD Stage 1)](#automated-testing-review-access-control-tdd-stage-1)
* [Limitations](#limitations)
* [Future Enhancements](#future-enhancements)
* [Real-Life Application & Project Continuity](#real-life-application--project-continuity)
* [Reflection](#reflection)
* [How to Use This Work](#how-to-use-this-work)


## Project Overview

The Django Fragrance Review App is a web application designed to showcase fragrance reviews within a clean, organised, and scalable Django framework. Developed as part of my ongoing progress in the Code Institute Level 5 Diploma, this project builds upon the foundations laid in my previous work—particularly the **“What’s Your Scent Spirit?”** fragrance quiz, which has been fully integrated into this site through a dedicated link on the homepage.

This project is not a standalone exercise; it is part of a growing ecosystem. The fragrance quiz integrates personality-driven scent recommendations powered by AI, while this Django review app focuses on user-generated reviews and structured content. Together, they form the early stages of a larger vision I plan to expand in the next milestone project.

Looking ahead, I intend for this Django application to evolve into the backbone of a more complete fragrance platform. Future features may include fragrance product listings, membership functionality, user accounts, or curated scent collections. This aligns closely with my long-term goal of building a real, usable fragrance-focused web experience that goes beyond coursework.

Fragrance is a personal special interest of mine, and this app represents the practical beginning of a project I fully intend to use beyond graduation—merging technical development with a genuine passion.

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
## Acknowledgments  

A heartfelt thank-you to my **Code Institute mentor** and my **University Centre Peterborough professor** for their continual guidance, encouragement, and focused feedback throughout the development of this Django project. Their support helped shape the project’s direction and ensured that each stage aligned with best practices and assessment standards.

I would also like to acknowledge the tools and resources that supported the build:

- **Django Documentation** – for clear, robust references while structuring models, views, and URLs.  
- **Heroku** – for providing a smooth setup for environment variables and PostgreSQL deployment.  
- **GitHub** – for version control and repository hosting throughout development.  
- **VS Code** – my primary environment for coding, testing, and refining features.  
- **Canva** – for creating and polishing visual assets that support the fragrance brand aesthetic.  
- **Stack Overflow & Django Community Forums** – for clarifying edge cases and troubleshooting unexpected behaviours.

Finally, this project builds upon the foundations of my earlier work — especially the *“What’s Your Scent Spirit?”* fragrance quiz — and I acknowledge how essential that project has been in shaping the visual identity and broader vision for this fragrance platform.

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
├── .venv/ # Virtual environment (ignored by Git)
├── my_project/ # Main Django project folder
│ ├── __pycache__/
│ ├── __init__.py
│ ├── .env # Environment variables (SECRET_KEY, DB settings)
│ ├── .gitignore
│ ├── asgi.py
│ ├── readme.md
│ ├── settings.py # Global Django configuration
│ ├── urls.py # Project-level URL routing
│ ├── wsgi.py # Entry point for deployment
│
├── reviews/ # Core fragrance reviews application
│ ├── __pycache__/
│ ├── migrations/ # Auto-generated database migrations
│ ├── static/
│ │ └── reviews/
│ │ ├── css/
│ │ │ └── reviews.css # Main stylesheet for reviews app
│ │ └── images/ # Image assets used within templates
│ ├── templates/
│ │ ├── registration/ # Auth templates (login/logout)
│ │ └── reviews/ # Review-related page templates
│ │ ├── base.html # Global layout (navbar, footer, blocks)
│ │ ├── home.html # Review list / homepage
│ │ ├── detail.html # Full review display
│ │ ├── new.html # Create new review form
│ │ ├── edit.html # Edit existing review
│ │ └── delete.html # Delete confirmation page
│ ├── __init__.py
│ ├── admin.py # Admin interface for Review model
│ ├── apps.py # App configuration
│ ├── forms.py # Django forms for create/edit
│ ├── models.py # Review model
│ ├── test.py
│ ├── tests.py
│ ├── urls.py # App-specific routing
│ └── views.py # View logic (list, detail, CRUD)
│
├── .gitignore
├── db.sqlite3 # Local development database
├── manage.py # Django management tool
├── Procfile # Heroku deployment configuration
├── requirements.txt # Python packages for deployment
└── runtime.txt # Python version specification

### Models  

The core data model for this project is intentionally simple and focused, providing a clean foundation for storing and displaying fragrance reviews while leaving room for future growth.

#### Review Model  

The `Review` model represents a single fragrance review entry in the database. It is responsible for capturing the key information needed to display each review on the site, and to support list, detail, edit, and delete views.

At a high level, the model stores:  
- A **title** to identify the review.  
- Main **review content** describing the fragrance experience.  
- Metadata such as **author/user** (where applicable) and timestamps for creation/updates.  

This model is connected to:  
- `admin.py` so reviews can be managed through the Django admin interface.  
- `views.py` to power the list, detail, edit, and delete views.  
- Templates in `templates/reviews/` to render reviews on the frontend.  

The model is deliberately kept lean at this stage so that it can be extended later with additional fields (for example: brand, scent family, rating, longevity, or occasion) as the project evolves into a more feature-rich fragrance platform.

### Views  

The application uses a set of focused views in `reviews/views.py` to handle the full lifecycle of a fragrance review:

- **Home view (`home`)** – Retrieves all `Review` objects and renders the main listing page using `home.html`.  
- **Detail view (`detail`)** – Loads a single `Review` by ID/primary key and displays its full content via `detail.html`.  
- **Create view (`new`)** – Presents a form for adding a new review and saves it if the submitted data is valid.  
- **Edit view (`edit`)** – Loads an existing review into a form, allowing the content to be updated.  
- **Delete view (`delete`)** – Confirms and processes the deletion of a review, then redirects back to the list.  

These views rely on the `Review` model, `forms.py`, and the templates under `templates/reviews/` to provide a complete CRUD workflow.

---

### Templates  

Templates are stored under `reviews/templates/` and organised into two folders:  

- `templates/reviews/` – Main app templates for the review functionality.  
- `templates/registration/` – Authentication-related templates (e.g., login/logout), used when restricting access to create/edit/delete actions.  

Within `templates/reviews/`, the key files are:

- **`base.html`** – The shared layout for the entire site, including the navigation bar, footer, hero section, and the main content block. All other templates extend this file.  
- **`home.html`** – The homepage and review listing view. Displays all reviews in a responsive grid of cards styled with `reviews.css`.  
- **`detail.html`** – Shows a single review in full, including title, body, and any metadata, along with Edit/Delete controls for authorised users.  
- **`new.html`** – Form template for creating a new review. Extends `base.html` and uses Django form tags to render fields cleanly.  
- **`edit.html`** – Form template for updating an existing review, visually consistent with `new.html` so create and edit feel like part of the same flow.  
- **`delete.html`** – Confirmation template for deleting a review, asking the user to confirm the action before it is finalised.  

Static assets for these templates (CSS and images) are stored under `reviews/static/reviews/`, including `reviews.css` and fragrance-related imagery.

---

### URLs  

URL configuration is split between the project-level `my_project/urls.py` and the app-level `reviews/urls.py`.

- **Project-level (`my_project/urls.py`)**  
  - Includes the `reviews` URL patterns, typically using:  
    ```python
    path("", include("reviews.urls"))
    ```  
  - Keeps the global routing file simple, delegating the detailed paths to the app.

- **App-level (`reviews/urls.py`)**  
  Defines named routes that map directly to the views and templates described above, for example:

  - `""` → `home` view → `home.html` (list of reviews)  
  - `"<int:pk>/"` → `detail` view → `detail.html`  
  - `"new/"` → `new` view → `new.html` (create review)  
  - `"<int:pk>/edit/"` → `edit` view → `edit.html`  
  - `"<int:pk>/delete/"` → `delete` view → `delete.html`  

  These named URL patterns are used throughout the templates with `{% url %}` tags, ensuring that navigation, Edit/Delete buttons, and redirects remain robust even if the exact paths change later.


## Design System & Typography
### Typography and Design System  

![WAVE Accessibility Results](/reviews/static/reviews/images/wave-accessibility.png) 

The design system for this Django fragrance review app continues the soft, elegant aesthetic established in the “What’s Your Scent Spirit?” quiz. The interface relies on pastel gradients, rounded shapes, gentle shadows, and subtle motion to create a warm, polished browsing experience.

#### Visual Style Overview  
- Soft colour gradients in pink and lavender tones.  
- Rounded containers and pill-shaped buttons.  
- Subtle hover and lift animations for interactivity.  
- Generous spacing for a calm, readable layout.  

#### Key Styled Components  

**Hero Section**  
A rounded gradient container (`#fbe9ff → #ffeef5`) with a fluid, responsive title and a bold CTA button in the brand’s signature purple (`#b45cda`). This section sets the visual tone for the site.

**Navigation Bar**  
A clean white bar with a lavender border, soft shadow, and responsive burger menu. Buttons and links follow the same purple accent colour and rounded “pill” aesthetic to maintain branding consistency.

**Review Cards**  
White cards with 1.25rem rounding, soft shadows, and a gentle hover-lift animation. The grid adapts automatically:  
- 1 column (mobile)  
- 2 columns (≥600px)  
- 3 columns (≥992px)

**Footer**  
Repeats the hero gradient for visual cohesion. Includes a fragrance-themed icon, spaced heading text, and soft-toned secondary text.

#### Typography  
- Headings use refined letter-spacing for an upscale feel.  
- Body text is clean, readable, and set with comfortable line-height.  
- Buttons use bold, rounded text for a modern, tactile appearance.

#### Responsive Design  
The entire layout is responsive: cards, nav menu, and text sizes all adjust smoothly to maintain usability across mobile, tablet, and desktop.

---


## Deployment

This project is deployed using GitHub for version control and Heroku for hosting the live Django application, with PostgreSQL configured as the production database.

---

### 1. Push Code to GitHub

Before deploying, ensure all changes are committed and pushed:

git add .
git commit -m "Prepare for deployment"
git push origin main

---

### 2. Add PostgreSQL on Heroku

Attach Heroku’s managed PostgreSQL database:

```heroku addons:create heroku-postgresql:hobby-dev```

This provides the DATABASE_URL used by Django in production.

---

### 3. Add Environment Variables

In Heroku → Settings → Config Vars, add:

- SECRET_KEY
- DATABASE_URL
- DEBUG = False

These values replace sensitive settings normally stored in your local .env file.

---

### 4. Prepare Project for Heroku

Ensure the repository includes:

- Procfile
- requirements.txt
- runtime.txt

Collect static files locally:

```python manage.py collectstatic```

This prepares all static assets (CSS, images, JS) for production.

---

### 5. Deploy Code

Deploy the project to Heroku:

```git push heroku main```

---

### 6. Run Migrations

Apply Django migrations in the Heroku environment:
```heroku run python manage.py migrate``

### Live App

The deployed Django Fragrance Review App is available at:

https://scentaholic-club-2c0a6bb0fd88.herokuapp.com/reviews/


## Future Enhancements

## Reflection


## Database Switch & Secret Key Security

## Database Configuration and Migration  

### Development Database: SQLite  

During early development, the project used **SQLite**, Django’s default lightweight file-based database.  
SQLite was chosen because it requires no setup, works seamlessly with Django’s ORM, and is ideal for rapid prototyping.

The database file (`db.sqlite3`) lived locally and was never committed to GitHub thanks to the `.gitignore` configuration.

---

### Production Database: PostgreSQL (Heroku)

For deployment, the project switched from SQLite to **PostgreSQL**, which is the recommended database engine for production Django applications.

PostgreSQL offers:

- Better performance under load  
- True concurrency support  
- More robust data integrity  
- Full compatibility with Heroku’s hosting environment  

Heroku automatically provides a `DATABASE_URL` environment variable once its PostgreSQL add-on is enabled.  
This replaces all local database settings when the app runs in production.

---

### Switching from SQLite to PostgreSQL  

The database switch was performed as part of deployment preparation:

1. Added Heroku Postgres:  
   `heroku addons:create heroku-postgresql:hobby-dev`

2. Removed the hardcoded database configuration from `settings.py` and replaced it with environment-based settings using:  
   - `DATABASE_URL`  
   - `dj_database_url` (parsed by Django)

3. Ensured that `db.sqlite3` remains local-only and **never** deployed or committed.

4. Ran migrations on Heroku to build the PostgreSQL schema:  
   `heroku run python manage.py migrate`

This cleanly migrated the app’s structure (not existing data) into the new production database.

---

### Environment Variables and Security  

The following environment variables were added to Heroku’s Config Vars to protect security-sensitive values:

- `SECRET_KEY`  
- `DATABASE_URL`  
- `DEBUG = False`  

These values are **never stored in GitHub**, ensuring best-practice separation of development and production environments.

---

### Outcome  

The application now uses:

- **SQLite** → locally for development  
- **PostgreSQL** → on Heroku for deployment  

This setup follows Django’s recommended production architecture and ensures stable, scalable performance for all database interactions within the Fragrance Review App.


## Testing and Validation  

### HTML & CSS Validation  

All HTML templates and CSS files used in the Django Fragrance Review App were validated to ensure semantic correctness, accessibility, and adherence to web standards.

---

#### HTML Validation (W3C Validator)  
Each template file located in `reviews/templates/reviews/` was tested using the W3C HTML Validator by pasting the rendered page source into the validation tool.

Validated templates:

- base.html  
- home.html  
- detail.html  
- new.html  
- edit.html  
- delete.html  

**Results:**  
- No critical HTML errors were found.  
- Warnings related to Django template tags (`{% %}`, `{{ }}`) were safely ignored since they are processed server-side.  
- All pages passed validation once Django syntax was accounted for.

---


#### CSS Validation (W3C CSS Validator)  
The stylesheet `reviews/static/reviews/css/reviews.css` was validated using the W3C CSS Validator.

**Results:**  
- No errors detected.  
- Minor warnings related to modern CSS features such as `clamp()` and gradient declarations were acceptable and intended.  
- CSS confirmed as clean, valid, and production-ready.

---
![W3C CSS Validator Results](/reviews/static/reviews/images/css-validator.png.png)

### Python & Django Checks  

The backend was validated using Django’s built-in system checks, migrations validation, and automated test suite.

---

#### Django “check” System  

The built-in Django system check was executed:

python manage.py check

**Results:**  
- No system check errors.  
- All installed apps and middleware passed validation.  
- No missing or conflicting configurations.

---

#### Django Migrations Check  

Checked for pending migrations:

python manage.py makemigrations --check

**Results:**  
- No model changes pending.  
- All migrations applied successfully.

---

#### Smoke Testing: Django Test Suite  

Lightweight smoke tests were created in `reviews/tests.py` to ensure that key views always load correctly and return the expected HTTP status codes.

Test code:

from django.test import TestCase
from django.urls import reverse
from .models import Review

class HomeViewSmokeTest(TestCase):
    def test_home_returns_200(self):
        url = reverse("reviews:home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

class DetailViewSmokeTest(TestCase):
    def setUp(self):
        self.review = Review.objects.create(
            brand="Khadlaj",
            fragrance_name="Fursan White",
            rating=4,
            body="Test body"
        )

    def test_detail_returns_200(self):
        url = reverse("reviews:detail", args=[self.review.pk])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

Command used to run tests:

python manage.py test reviews

**Result:**

Found 2 tests.
..
----------------------------------------------------------------------
Ran 2 tests in 0.024s

OK

These tests confirm that both the homepage and individual review detail pages load successfully with status code 200, ensuring essential routes remain functional after updates, deployment changes, or database resets.

---


### Manual Functional Testing  

### Login, Logout, and Signup Tests  

Comprehensive manual testing was performed on the user authentication system, including signup, login, logout, and message feedback. These tests confirmed correct session handling and template rendering using Django’s authentication flow.

---

#### Manual Workflow Testing (Browser)

1. Navigated to `/accounts/signup/`  
   - Filled out the registration form with a new username and password.  
   - ✔️ User account created successfully.  
   - ✔️ Redirected to the **Sign in** page.

2. Navigated to `/accounts/login/`  
   - Entered **correct credentials** → ✔️ Redirected to `/reviews/`.  
   - Entered **incorrect password** → ⚠️ Displayed validation message:  
     *“Check your username/password and try again.”*

3. Tested logout workflow  
   - Clicked **Sign out** → ✔️ Redirected to the reviews homepage.  
   - Verified that the session ended correctly.  
   - Navigation updated to show **Sign in / Create account** instead of user options.

---

![Chrome DevTools Console – No Errors](/reviews/static/reviews/images/chrome-console.png)

#### Django Messages Framework Validation  

Confirmed that the login and logout events trigger messages correctly and that they display inside the template.

Django template snippet used:

{% if messages %}
  <div class="messages">
    {% for message in messages %}
      <p class="alert">{{ message }}</p>
    {% endfor %}
  </div>
{% endif %}

Messages displayed successfully for:

- Successful login  
- Incorrect login attempt  
- Successful logout  

All authentication tests passed with correct redirects, session handling, and UI feedback.

### Automated Testing: Review Access Control (TDD Stage 1)  

This testing phase introduced **Test Driven Development (TDD)** for the new *Post Review* feature.  
Before creating any form logic or templates, automated tests were written to confirm that access control behaved correctly.

A dedicated test suite (`reviews/test.py`) was added to verify:

- Anonymous users are **redirected** to the login page when accessing `/reviews/new/`.  
- Logged-in users can successfully access the page (`HTTP 200 OK`).  

---

#### TDD Test Code (Initial Failing Tests)

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class NewReviewAccessTest(TestCase):
    def test_anonymous_is_redirected_to_login(self):
        resp = self.client.get(reverse("reviews:new"))
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/accounts/login/", resp.headers["Location"])

    def test_logged_in_gets_200(self):
        User.objects.create_user(username="alice", email="a@example.com", password="pw12345")
        self.client.login(username="alice", password="pw12345")
        resp = self.client.get(reverse("reviews:new"))
        self.assertEqual(resp.status_code, 200)

---

#### Initial Result  

The tests **failed** with a `NoReverseMatch` error:

- The route `reviews:new` did not exist yet  
- No corresponding view was implemented  
- No template (`new.html`) was present  

This failure correctly confirmed that the tests were written **before** implementation — matching the TDD philosophy.

---

#### Implementation Steps (to satisfy the failing tests)

The minimal implementation required to make the tests pass included:

- Adding a new view (`new`) inside `reviews/views.py`, protected with `@login_required`  
- Defining the route `/reviews/new/` in `reviews/urls.py`  
- Creating a placeholder template `new.html` under `reviews/templates/reviews/`  

This satisfied the access-control logic without adding full review creation functionality yet — aligning perfectly with TDD’s “small steps” approach.

---

#### Final Outcome  

After implementing the minimal logic:

- ✔️ Anonymous users were correctly redirected to `/accounts/login/`  
- ✔️ Logged-in users received `HTTP 200`  
- ✔️ All six tests passed successfully  
- ✔️ Authentication gating and secure routing were fully validated  

---

#### Test Execution  

The full suite was executed locally using:

python manage.py test reviews

**Result:**

All tests passed successfully.

---

This TDD phase ensured that the *Post Review* feature was built on secure, predictable authentication behavior before any further development took place.
### Testing Evidence (Screenshots)  

The following screenshots were captured during testing to provide visual evidence of validation, code quality checks, and runtime stability:

- **Django Tests – Terminal Output**  
  Full output from running the Django test suite, confirming that all configured tests executed and passed successfully.  
  ![Django Tests – Terminal Output](/reviews/static/reviews/images/django-tests.png)

- **Django Tests Running OK**  
  A focused view of the final test summary (`OK`), showing that the core smoke tests and access-control tests completed without failures.  
  ![Django Tests Running OK](/reviews/static/reviews/images/django-tests-ok.png)

- **Flake8 Linting Results**  
  Evidence of Python code quality checks using Flake8, confirming that there are no critical style or syntax issues in the key Django files.  
  ![Flake8 Linting Results](/reviews/static/reviews/images/flake8-linting.png)

- **Nu HTML Validator Results**  
  Results from the Nu HTML Validator, showing that the rendered HTML for the core templates passes validation once Django template tags are accounted for.  
  ![Nu HTML Validator Results](/reviews/static/reviews/images/nu-html-validator.png)

- **W3C CSS Validator Results**  
  Screenshot from the W3C CSS Validator confirming that the main stylesheet (`reviews.css`) contains no errors and only acceptable modern-CSS warnings.  
  ![W3C CSS Validator Results](/reviews/static/reviews/images/css-validator.png)

- **Chrome DevTools Console – No Errors**  
  Browser console output captured during manual testing, showing no JavaScript errors or warnings while navigating the key views (home, detail, login, logout).  
  ![Chrome DevTools Console – No Errors](/reviews/static/reviews/images/chrome-console.png)

- **WAVE Accessibility Results**  
  Accessibility scan of the main pages using the WAVE tool, demonstrating that the interface has no critical accessibility issues and follows basic accessibility best practices.  
  ![WAVE Accessibility Results](/reviews/static/reviews/images/wave-accessibility.png)


## Future Enhancements  

As the project grows, the next realistic step is to evolve it into a **Fragrance Club** with membership features and curated product offerings. These enhancements build naturally on the current structure:

---

### 1. Membership System  
Introduce user membership with simple perks such as saved reviews, personalised recommendations, and access to member-only content.

---

### 2. Real Fragrance Product Listings  
Add a product model so users can browse actual perfumes alongside reviews, including brand, concentration, price tier, and links to retailers.

---

### 3. Quiz Integration  
Connect the existing “What’s Your Scent Spirit?” quiz to the platform so users receive suggested products or reviews based on their quiz results.

---

### 4. Personal Dashboard  
Provide a minimal dashboard where members can view their reviews, saved fragrances, and quiz outcomes.

---

### 5. Light Ecommerce Direction  
Without implementing payments yet, introduce affiliate links or a curated “shop” page to begin shaping the commercial side of the Fragrance Club.

---

These enhancements keep the project realistic while moving toward the long-term vision of a personalised, membership-based fragrance platform.
## Limitations  

The Django Fragrance Review App is intentionally scoped to stay clear, assessable, and stable. While fully functional, it includes several practical limitations that create space for future development.

---

### 1. Simplified Review Model  
The current review system focuses only on essential fields. It does not yet include richer fragrance data such as longevity, seasonality, projection, or note structure. This keeps the app straightforward but limits how detailed reviews can be.

---

### 2. Basic User Accounts  
Authentication works reliably, but the user system is minimal:

- No profile editing  
- No avatar or saved fragrances  
- No password reset flow  

These features are not required at this stage but will be essential when evolving the platform into a full Fragrance Club.

---

### 3. No Full Product or Membership System Yet  
Although the long-term plan involves a membership model and curated product listings, this version does not yet include:

- Product catalogue  
- Membership tiers  
- Personal dashboards  
- Ecommerce or affiliate integration  

These are reserved for the next project phase.

---

### 4. Limited Automated Testing  
Testing covers:

- Smoke tests  
- Access control tests  
- Manual authentication tests  

However, deeper coverage (form edges, failure states, regression tests) is still limited, which is acceptable for the project scope but not production-grade.

---

### 5. Heroku Hosting Constraints  
The project uses a **paid Heroku PostgreSQL database**, which ensures reliability.  
However, Heroku’s platform still has limits compared to dedicated production hosting, such as:

- Slower cold starts  
- Limited dyno resources  
- Basic logging compared to advanced observability tools  

These are acceptable trade-offs for a coursework project but would need scaling for a commercial platform.

---

Overall, these limitations do not reduce the project’s effectiveness or stability—they simply reflect its current stage of development and clarify clear, achievable next steps.```

## Reflection  

During the development of this Django project, I encountered several issues that became valuable learning experiences — especially around environment management, file structure, and protecting sensitive data.

---

### Secret Key Exposure and Git Hygiene  

Early in the project, the Django `SECRET_KEY` was accidentally pushed to GitHub because my `.gitignore` file was not configured correctly. As a result, environment files and other sensitive settings were tracked by Git and committed before I noticed the mistake.

Fixing this required several steps:

- Removing the exposed key from version history  
- Rotating the key to a new secure value  
- Moving all secrets into a dedicated `.env` file  
- Updating `settings.py` to load configuration using environment variables  
- Correcting the `.gitignore` so that `.env`, `db.sqlite3`, compiled files, and virtual environments are always ignored  

This process helped me clearly understand why Django projects should **never** rely on hard-coded values and how easily a small oversight can lead to a serious security risk. I now feel far more confident in configuring environment variables and protecting credentials — skills I will take with me into my final project and future professional work.

---

### Project Folder Location & OneDrive Interference  

Another significant issue came from storing the project inside a OneDrive-synchronised folder. This caused:

- random file locking  
- environment conflicts  
- path inconsistencies  
- problems activating the virtual environment  
- Git changes being detected inconsistently because of background syncing  

The constant interference made the development environment unstable and unpredictable.

To resolve this, I moved the entire project into a standard, non-synced directory on my local machine. Once relocated, all issues disappeared: the virtual environment behaved consistently, migrations ran correctly, tests stopped breaking, and Git stopped detecting phantom file changes.

This taught me how important it is to keep development projects **outside of cloud-synced folders**, as tools like OneDrive, iCloud, or Dropbox can silently disrupt workflows and corrupt virtual environments.

---

### Lessons Learned  

These challenges ultimately strengthened my understanding of:

- secure key management  
- proper `.gitignore` configuration  
- the difference between development and production settings  
- safe database handling  
- choosing the right location for local projects  
- troubleshooting version control and environment issues  

Although stressful in the moment, each problem forced me to slow down, investigate carefully, and implement a more professional setup. As a result, I now feel much more prepared for the final project and more confident managing a full Django environment from development through deployment.

This project has not only improved my technical skills but also given me a deeper appreciation for the structure, discipline, and attention to detail required in backend development.
