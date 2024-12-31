# Contributing to QuGenAI

We welcome contributions to QuGenAI! To ensure a consistent and high-quality codebase, we’ve established the following guidelines, adapted from Sentry’s documentation. We acknowledge Sentry’s comprehensive guidelines and have tailored them to fit our project’s current needs. As QuGenAI evolves, we plan to develop our own detailed guidelines.

## Acknowledgement

These guidelines are adapted from Sentry’s [Development Philosophy](https://develop.sentry.dev/getting-started/philosophy/) as well as their Engineering Practices for [Commit Messages](https://develop.sentry.dev/engineering-practices/commit-messages/) and [Code Review](https://develop.sentry.dev/engineering-practices/code-review/). We appreciate their comprehensive documentation and have tailored it to fit QuGenAI’s current needs. As our project evolves, we plan to develop our own detailed guidelines.

## Branches and Pull Requests

We have a **simple and flexible branching model** inspired by Sentry’s [Development Philosophy](https://develop.sentry.dev/getting-started/philosophy/):

- **Mainline Branch**: The `main` branch is always **deployable** and **green** (tests pass). Any commit that lands on `main` must be production-ready.

    > ⭐️ This is the most important rule: mainline stays green. Any commit that ends up on the mainline will be deployed.

- **Feature Branches**: Feature development, bug fixes, and other changes happen on **feature branches** based on `main`. We do not enforce rigid naming conventions for branches at this time We expect branch naming conventions to evolve naturally as the project grows, and they may be formalized later. Use names that make sense and help identify the purpose of the branch. Some common prefixes and naming patterns include:

  - Branches tied to GitHub issues:

    ```text
    123-feature-description
    456-fix-login-bug
    ```

  - Branches for features, fixes, and chores:

    ```text
    feature/authentication
    fix/db-connection-error
    chore/update-dependencies
    ```

  - Branches for experiments and spikes:

    ```text
    experiment/ai-model
    spike/optimization
    ```

- **Pull Requests (PRs)**:
  - Open a pull request (PR) from your **feature branch** into `main`.
  - Use **Draft PRs** for work in progress and **standard PRs** for review-ready code.
  - Keep PRs **focused and small** whenever possible.

- **Tests Must Pass**: Every PR must pass all tests and linters before being merged into `main`.

- **Rebase Before Merge**: Always rebase your branch onto the latest `main` before merging. Avoid merge commits unless necessary.

## Commit Messages

Clear and consistent commit messages are crucial for maintaining an understandable project history. Please adhere to the following rules:

1. Separate subject from body with a blank line
2. Limit the subject line to 60 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Use the body to explain what and why vs. how
7. Wrap the body at about 72 characters per line
8. Each commit should be a single, stable change

## Commit Message Format

Each commit message should consist of a header, a body, and an optional footer. The header includes a type, an optional scope, and a subject:

```text
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

- **Type**: Describes the nature of the change. Must be one of the following:
  - **feat**: A new feature
  - **fix**: A bug fix
  - **docs**: Changes to documentation only
  - **style**: Changes that do not affect the meaning of the code (white-space, formatting, sorting imports, etc.)
  - **refactor**: A code change that neither fixes a bug nor adds a feature
  - **test**: Adding missing tests or correcting existing tests
  - **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation
  - **perf**: A code change that improves performance
  - **build**: Changes that affect the build system or external dependencies (e.g., Python, Heroku)
  - **ci**: Changes to our CI configuration files and scripts
  - **meta**: Changes to meta information in the repo (e.g., owner files, editor config)
  - **license**: Changes to licenses
- **Scope**: The name of the core component affected (e.g., ai, api, auth). This is optional. As the project grows, we will define scopes for each component.
- **Subject**: A brief description of the change:
  - Use the imperative, present tense: “change” not “changed” nor “changes”
  - Capitalize the first letter
  - Do not end with a period
- **Body**: Explain the motivation for the change and contrast it with previous behavior.
- **Footer**: Reference any relevant GitHub issues. Use the `Closes #<issue>` or `Fixes #<issue>` syntax to automatically close the issue when the pull request is merged.

Example commit message:

```text
docs: Add contribution guidelines

Add a new section to the README with information on how to contribute
to this project. Also, add a new file with the guidelines themselves
with attribution to Sentry’s guidelines.

Closes #9
```

## Branching and Merging Workflow

We use a rebase workflow to maintain a linear project history. This means:

- Rebase: Before merging, rebase your branch onto the latest main to incorporate upstream changes.
- Squash Commits: Combine multiple related commits into a single commit to ensure each commit is a clear, functional, and stable change.
- Rebase and Merge: Use the “Rebase and Merge” option when merging pull requests to avoid unnecessary merge commits.

When squashing commits, ensure you update the commit message to follow the commit message guidelines. If you’re working locally, it can be useful to --amend a commit or utilize rebase -i to reorder, squash, and reword your commits (see recommended resourcce below to master these skills).

## Code Review

As the projects grows beyond a solo developer, code review will become mandatory for all changes. It helps maintain code quality and facilitates knowledge sharing.

- Reviewers: Assign at least one reviewer to your pull request.
- Tests: Ensure that your changes are covered by appropriate tests.
- Documentation: Update documentation as necessary to reflect your changes.

For more detailed guidelines on code reviews, please refer to Sentry’s Code Review guidelines.

## Documentation

Clear documentation is essential for both users and contributors. When making changes:

- Update Documentation: Ensure that any relevant documentation is updated to reflect your changes.
- Follow Style Guidelines: Adhere to the project’s style guidelines for documentation.

For more detailed guidelines on documentation, please refer to Sentry’s Documentation guidelines.

## Recommended Resource

Adam Johnson's [Boost Your Git DX](https://adamchainz.gumroad.com/l/bygdx) book covers a wide range of topics, including **commit messages**, **interactive rebasing**, and **squashing commits**, which align well with our adopted Sentry's guidelines.

Thank you for contributing to QuGenAI!
