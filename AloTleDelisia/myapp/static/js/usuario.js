function toggleSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section.style.display === 'block') {
      section.style.display = 'none';
    } else {
      section.style.display = 'block';
    }
  }
  