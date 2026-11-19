# Contributing to ReachJobAI

Thank you for your interest in contributing to ReachJobAI! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/reach-job-ai.git
   cd reach-job-ai
   ```
3. **Set up the development environment**:
   - Backend: Follow instructions in README.md
   - Frontend: Follow instructions in README.md

## 📋 Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Adding or updating tests

### 2. Make Your Changes

- Write clean, maintainable code
- Follow existing code style
- Add comments for complex logic
- Update documentation as needed

### 3. Test Your Changes

**Backend**:
```bash
cd backend
.\venv\Scripts\Activate.ps1
pytest
```

**Frontend**:
```bash
cd frontend
npm run type-check
npm run lint
npm run build
```

### 4. Commit Your Changes

Follow conventional commit format:

```bash
git commit -m "feat: add user authentication endpoint"
git commit -m "fix: resolve CORS issue in production"
git commit -m "docs: update API documentation"
```

Commit types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Formatting, missing semicolons, etc.
- `refactor:` - Code restructuring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title and description
- Link to related issues
- Screenshots/GIFs for UI changes

## 💻 Code Style Guidelines

### Python (Backend)

- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use Black for formatting: `black app/`
- Use Ruff for linting: `ruff check app/`

### TypeScript (Frontend)

- Use TypeScript strict mode
- Avoid `any` type
- Use meaningful variable names
- Follow React best practices
- Use functional components with hooks

## 🧪 Testing Guidelines

- Write tests for new features
- Maintain or improve code coverage
- Test edge cases
- Mock external services

## 📝 Documentation

- Update README.md if adding features
- Add docstrings to Python functions
- Add JSDoc comments to TypeScript functions
- Update API documentation

## 🐛 Reporting Bugs

When reporting bugs, include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Detailed steps
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: OS, Python version, Node version
6. **Screenshots**: If applicable

## 💡 Suggesting Features

When suggesting features, include:

1. **Use Case**: Why is this needed?
2. **Proposed Solution**: How should it work?
3. **Alternatives**: Other approaches considered
4. **Additional Context**: Mockups, examples, etc.

## 🔒 Security

- Never commit sensitive data (.env files, API keys, passwords)
- Report security vulnerabilities privately
- Follow secure coding practices

## ⚖️ Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## 📬 Questions?

Feel free to:
- Open an issue for discussion
- Ask questions in pull requests
- Contact the maintainers

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project credits

Thank you for contributing to ReachJobAI! 🚀
