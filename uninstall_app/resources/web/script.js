function adjustFooter() {
    const bodyHeight = document.body.offsetHeight;
    const viewportHeight = window.innerHeight;
    const footer = document.querySelector('footer');
    if (bodyHeight < viewportHeight) {
      footer.style.position = 'fixed';
      footer.style.bottom = '0';
      footer.style.width = '100%';
    } else {
      footer.style.position = 'static';
    }
  }

  window.addEventListener('load', adjustFooter);
  window.addEventListener('resize', adjustFooter);