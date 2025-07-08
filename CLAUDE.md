# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based academic website for the Autonomous Navigation and Perception Lab (ANPL) at Technion – Israel Institute of Technology. The site showcases research projects, team members, publications, and student projects using the bulma-clean-theme.

## Development Commands

### Local Development
```bash
# Install dependencies
bundle install

# Start local development server
bundle exec jekyll serve

# Build the site
bundle exec jekyll build
```

### Publication Management
```bash
# Generate publication files by research topic
cd _bibliography
./anpl_generate_pubs.sh
```

## Architecture & Structure

### Core Collections
- `_research/` - Research project pages with YAML frontmatter defining titles, images, and descriptions
- `_team/` - Team member profiles with categories (staff, phd_students, master_student, etc.)
- `_student-projects/` - Student project descriptions and requirements
- `_bibliography/` - BibTeX files and publication management scripts

### Key Layout Templates
- `research.html` - Two-column layout with image and description for research projects
- `team_member_personal_page.html` - Individual team member pages
- `default_for_research.html` - Base template for research-related pages

### Content Organization
- Research projects use `research_code` field for categorization
- Team members use `category` field with predefined order: staff, phd_students, master_student, undergraduate_students, visiting_students
- Publications managed through jekyll-scholar plugin with custom CSL styling

### Bibliography System
- Main bibliography: `_bibliography/VadimIndelman.bib`
- Research-specific bibliographies generated in `_bibliography/research-projects-bib/`
- Python scripts for filtering and processing BibTeX entries
- Custom IEEE citation style via `_bibliography/ieee.csl`

### Asset Management
- Images organized by type: `/img/research/`, `/img/team/`, `/img/funding/`
- Publications stored in `/Publications/` directory
- Bulma CSS framework with custom SCSS in `_sass/`

## Development Notes

- Jekyll 4.3.2 with Ruby dependencies managed via Gemfile
- Uses remote_theme for bulma-clean-theme
- Scholar plugin configured for bibliography management with year-based sorting
- Collections output enabled for research, team, and student-projects
- Google Analytics integration configured
- Responsive design with Bulma CSS framework