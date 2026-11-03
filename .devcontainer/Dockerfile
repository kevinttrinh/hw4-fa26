# Development environment for COSI 106B HW4.
#
# You do not need to build this yourself. It is built and published to
# ghcr.io/brandeis-cosi-106b/hw4-fa26 by .github/workflows/build-image.yml, and
# .devcontainer/devcontainer.json simply *pulls* the finished image.
#
# Ubuntu 22.04 matches the Gradescope autograder's base image.
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Keep in sync with the exports at the top of install-tools.sh.
# The virtualenv's bin/ is first on PATH, so `python` and `ruff` are simply
# available. Nothing to activate or install per container.
ENV UV_PYTHON_INSTALL_DIR=/opt/uv/python \
    UV_CACHE_DIR=/opt/uv/cache \
    UV_PROJECT_ENVIRONMENT=/opt/uv/venv \
    UV_LINK_MODE=copy \
    VIRTUAL_ENV=/opt/uv/venv \
    PATH=/opt/uv/venv/bin:$PATH

COPY .devcontainer/install-tools.sh /tmp/install-tools.sh
RUN bash /tmp/install-tools.sh && rm /tmp/install-tools.sh

# The `hunch` command runs Hunch from whatever repository you are in, with that
# repository's src/ on the path.
COPY .devcontainer/hunch /usr/local/bin/hunch
RUN chmod 0755 /usr/local/bin/hunch

# `bundle-history` saves a student's commit history for submission.
COPY .devcontainer/bundle-history /usr/local/bin/bundle-history
RUN chmod 0755 /usr/local/bin/bundle-history

# Install the locked Python dependencies (versions pinned in uv.lock), then
# smoke-test the toolchain. If a dependency can't be installed on this
# platform, the image build fails here instead of on a student's laptop.
COPY pyproject.toml uv.lock .python-version /tmp/deps/
RUN cd /tmp/deps \
    && uv sync --dev --frozen --no-install-project \
    && cd / && rm -rf /tmp/deps \
    && python -c "import click, jinja2, markdown, yaml" \
    && ruff --version \
    && git --version \
    && less --version \
    && chmod -R a+rwX /opt/uv
