# CLAUDE.MD - Project Documentation for AI Assistants

## Project Overview

**30days-i18n** is an internationalized (i18n) version of the #30DaysOfStreamlit coding challenge. This repository hosts a Streamlit web application that presents a 30-day learning challenge for building Streamlit applications, available in multiple languages.

**Official Challenge**: `#30DaysOfStreamlit` - a 30-day social challenge to learn, build and deploy Streamlit apps.

## Repository Structure

```
30days-i18n/
├── .devcontainer/          # Development container configuration
├── content/                # Markdown content for daily challenges (per language)
│   ├── bn/                # Bengali content
│   ├── de/                # German content
│   ├── en/                # English content
│   ├── es/                # Spanish content
│   ├── fr/                # French content
│   ├── hi/                # Hindi content
│   ├── ja/                # Japanese content
│   ├── pl/                # Polish content
│   ├── pt/                # Portuguese content
│   ├── ru/                # Russian content
│   └── zh/                # Chinese content
├── locale/                 # Translation files for UI elements
├── readmes/               # README files in various languages
├── streamlit_app.py       # Main application file
├── language_constants.py  # Language configuration
└── requirements.txt       # Python dependencies
```

## Tech Stack

- **Framework**: Streamlit
- **Language**: Python 3.x
- **Key Dependencies**:
  - streamlit
  - pandas
  - Pillow (PIL)
- **Internationalization**: Using Streamlit's built-in locale system

## Key Files

### streamlit_app.py
Main application file (102 lines) that:
- Sets up page configuration with wide layout
- Implements language selection via session state
- Loads daily challenge content from markdown files
- Provides navigation between 30 days
- Displays content with images and figures
- Uses Streamlit's `gettext` for UI translations

### language_constants.py
Configuration file for supported languages and their metadata.

### content/{language}/*.md
Daily challenge content files (Day1.md through Day30.md) for each supported language.

## Supported Languages

1. English (en)
2. Bengali (বাংলা - bn)
3. German (Deutsch - de)
4. French (français - fr)
5. Hindi (हिन्दी - hi)
6. Japanese (日本語 - ja)
7. Russian (русский - ru)
8. Portuguese (português - pt)
9. Chinese (中文 - zh)
10. Polish (polski - pl)
11. Spanish (español - es)

## Development Setup

### Prerequisites
- Python 3.x
- pip package manager
- Basic understanding of Streamlit

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run streamlit_app.py
```

### Local Development with Dev Container
The repository includes a `.devcontainer` configuration for consistent development environments.

## Content Structure

### Daily Challenges Organization
- Days 1-7: Beginner level
- Days 8-23: Intermediate level
- Days 24-30: Advanced level

### Challenge Topics Include
- Setting up local and cloud environments
- Installing Streamlit
- Learning Streamlit commands
- Session state management
- Data and memory management via caching
- Complex layouts
- Deployment strategies

## Adding New Content

### Adding a New Language

1. **Add language to constants**:
   - Update `language_constants.py` with new language code and metadata

2. **Create content directory**:
   ```bash
   mkdir -p content/{language_code}
   mkdir -p content/{language_code}/images
   mkdir -p content/{language_code}/figures
   ```

3. **Translate daily challenges**:
   - Create Day1.md through Day30.md in the new language directory
   - Add corresponding images and CSV files for figures if needed

4. **Add locale translations**:
   - Create locale files for UI text translations in `locale/{language_code}/`

5. **Create README**:
   - Add translated README in `readmes/{language_code}/README.md`

6. **Update main README**:
   - Add language link to root `README.md`

### Adding or Modifying Daily Content

1. Navigate to appropriate language folder: `content/{language}/`
2. Edit or create `Day{N}.md` file (where N is 1-30)
3. Add images to `content/{language}/images/` if needed
4. Create CSV in `content/{language}/figures/Day{N}.csv` for figure metadata

## Important Patterns

### Language Selection
The app uses `st.session_state["language"]` to track the current language selection.

### Query Parameters
The app supports URL query parameters for deep linking:
- `?challenge=Day5` - Opens specific day

### Content Loading
Content is dynamically loaded from markdown files based on:
1. Selected language (from session state)
2. Selected day (from selectbox or query params)

### Translation System
- UI elements use `gettext as _` for translations
- Format: `_("String to translate").format(param=value)`
- Example: `_("Day {day}").format(day=1)`

## Common Development Tasks

### Testing a Specific Day
```python
# Modify query params in URL
?challenge=Day15
```

### Adding Images to Content
1. Place image in `content/{language}/images/`
2. Reference in markdown: `![Description](images/filename.png)`
3. Or use figures CSV system for captioned images

### Debugging Language Issues
Check that:
- Session state has valid language code
- Content directory exists for that language
- All Day{N}.md files are present (1-30)

## Known Dependencies

The project includes a bundled wheel file:
- `streamlit-1.21.0-py2.py3-none-any.whl`

Note: `requirements.txt` specifies `numpy==1.26.4` (pinned version)

## Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Official #30DaysOfStreamlit App](https://share.streamlit.io/streamlit/30days/)
- [Streamlit Twitter](https://twitter.com/streamlit)
- [Streamlit LinkedIn](https://www.linkedin.com/company/streamlit/)

## Contributing Guidelines

When contributing to this repository:

1. Ensure translations maintain the same structure and meaning as English source
2. Test the app with your changes: `streamlit run streamlit_app.py`
3. Verify all 30 days display correctly for modified languages
4. Keep markdown formatting consistent across languages
5. Add appropriate metadata (images, figures CSV) when referenced in content
6. Follow existing naming conventions (Day1.md, Day2.md, etc.)

## Deployment

This app can be deployed using:
- [Streamlit Community Cloud](https://streamlit.io/cloud)
- Any Python hosting platform that supports Streamlit

### Streamlit Cloud Deployment
1. Push code to GitHub
2. Connect repository to Streamlit Community Cloud
3. Specify `streamlit_app.py` as the main file
4. Deploy

## License

See LICENSE file for details (currently MIT License based on repository).

---

**Last Updated**: 2026-01-03
**Maintained By**: This is a community-driven internationalization project
**Base Project**: [30 Days of Streamlit](https://github.com/streamlit/30days)
