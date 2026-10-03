/* WAJHA site behavior: nav, scroll effects, reveal/count-up animation, contact form.
 * Plain JS, no framework, no dependencies. */
(function () {
  "use strict";

  /* ---------- Mobile nav ---------- */
  var toggle = document.getElementById("nav-toggle");
  var nav = document.getElementById("main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------- Sticky header shadow ---------- */
  var header = document.getElementById("site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Back to top ---------- */
  var backToTop = document.getElementById("back-to-top");
  if (backToTop) {
    var onScrollTop = function () {
      backToTop.classList.toggle("is-visible", window.scrollY > 480);
    };
    window.addEventListener("scroll", onScrollTop, { passive: true });
    onScrollTop();
    backToTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------- Scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if (revealEls.length) {
    if ("IntersectionObserver" in window) {
      var revealObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add("is-visible");
              revealObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
      );
      revealEls.forEach(function (el) { revealObserver.observe(el); });
    } else {
      revealEls.forEach(function (el) { el.classList.add("is-visible"); });
    }
  }

  /* ---------- Count-up stats ---------- */
  var counters = document.querySelectorAll(".count-up");
  if (counters.length) {
    var animateCount = function (el) {
      var target = parseInt(el.getAttribute("data-target"), 10) || 0;
      var duration = 1400;
      var start = null;
      var step = function (timestamp) {
        if (start === null) start = timestamp;
        var progress = Math.min((timestamp - start) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(eased * target).toString();
        if (progress < 1) {
          window.requestAnimationFrame(step);
        } else {
          el.textContent = target.toString();
        }
      };
      window.requestAnimationFrame(step);
    };
    if ("IntersectionObserver" in window) {
      var countObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              animateCount(entry.target);
              countObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.4 }
      );
      counters.forEach(function (el) { countObserver.observe(el); });
    } else {
      counters.forEach(function (el) { el.textContent = el.getAttribute("data-target"); });
    }
  }

  /* ---------- Contact form (Formspree) ----------
   * Replace YOUR_FORM_ID below AND on the form's data-formspree-endpoint
   * attribute in /en/contact.html and /ar/contact.html with your real
   * Formspree endpoint (https://formspree.io/f/xxxxxxxx). See README.md. */
  var form = document.getElementById("contact-form");
  if (form) {
    var status = document.getElementById("form-status");
    var submitBtn = form.querySelector(".form-submit");
    var submitLabel = form.querySelector(".form-submit-label");
    var defaultLabel = submitLabel ? submitLabel.textContent : "";
    var endpoint = form.getAttribute("data-formspree-endpoint") || "";

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (!status) return;

      if (!endpoint || endpoint.indexOf("YOUR_FORM_ID") !== -1) {
        status.textContent = status.getAttribute("data-setup-error");
        status.className = "form-status is-error";
        return;
      }

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      submitBtn.disabled = true;
      if (submitLabel) submitLabel.textContent = status.getAttribute("data-sending");
      status.textContent = status.getAttribute("data-sending");
      status.className = "form-status";

      fetch(endpoint, {
        method: "POST",
        headers: { Accept: "application/json" },
        body: new FormData(form),
      })
        .then(function (response) {
          if (response.ok) {
            status.textContent = status.getAttribute("data-success");
            status.className = "form-status is-success";
            form.reset();
          } else {
            status.textContent = status.getAttribute("data-error");
            status.className = "form-status is-error";
          }
        })
        .catch(function () {
          status.textContent = status.getAttribute("data-error");
          status.className = "form-status is-error";
        })
        .finally(function () {
          submitBtn.disabled = false;
          if (submitLabel) submitLabel.textContent = defaultLabel;
        });
    });
  }
})();
