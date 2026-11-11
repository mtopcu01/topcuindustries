/* Topcu Industries — site behaviour (no dependencies) */
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Mobile nav */
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && header.classList.contains("nav-open")) {
        header.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* Header border on scroll */
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* Reveal on scroll */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* Hero terminal */
  var term = document.getElementById("term");
  if (term) {
    var lines = [
      [["t-prompt", "$ "], ["", "topcu engage --scope external,web,m365"]],
      [["t-dim", "[*] rules of engagement signed"]],
      [["t-ok", "[+] "], ["", "recon complete · 23 hosts, 4 web apps"]],
      [["t-warn", "[!] "], ["", "MFA not enforced on legacy mail"]],
      [["t-crit", "[!!] "], ["", "exposed admin panel · CRITICAL"]],
      [["t-ok", "[+] "], ["", "critical finding escalated to client"]],
      [["t-ok", "[+] "], ["", "report delivered · fixes prioritized"]],
      [["t-ok", "[+] "], ["", "retest passed · attestation issued"]],
      [["t-prompt", "$ "]]
    ];
    var pre = term;
    pre.textContent = "";
    var cursor = document.createElement("span");
    cursor.className = "t-cursor";

    var addSeg = function (line, cls, text) {
      var s = document.createElement("span");
      if (cls) s.className = cls;
      s.textContent = text;
      line.appendChild(s);
      return s;
    };

    if (reduceMotion) {
      lines.forEach(function (segs, i) {
        segs.forEach(function (sg) { addSeg(pre, sg[0], sg[1]); });
        if (i < lines.length - 1) pre.appendChild(document.createTextNode("\n"));
      });
      pre.appendChild(cursor);
    } else {
      var li = 0;
      var nextLine = function () {
        if (li >= lines.length) { pre.appendChild(cursor); return; }
        var segs = lines[li];
        var isCmd = li === 0;
        if (li > 0) pre.appendChild(document.createTextNode("\n"));
        if (isCmd) {
          addSeg(pre, segs[0][0], segs[0][1]);
          var target = addSeg(pre, segs[1][0], "");
          pre.appendChild(cursor);
          var full = segs[1][1], ci = 0;
          var typer = setInterval(function () {
            target.textContent = full.slice(0, ++ci);
            if (ci >= full.length) {
              clearInterval(typer);
              pre.removeChild(cursor);
              li++; setTimeout(nextLine, 450);
            }
          }, 28);
        } else {
          segs.forEach(function (sg) { addSeg(pre, sg[0], sg[1]); });
          li++; setTimeout(nextLine, li === lines.length - 1 ? 300 : 520);
        }
      };
      setTimeout(nextLine, 500);
    }
  }

  /* Contact form */
  var form = document.getElementById("quote-form");
  if (form) {
    // Pre-select a service from ?service=slug
    var params = new URLSearchParams(window.location.search);
    var pre = params.get("service");
    if (pre) {
      var box = form.querySelector('input[name="services"][data-slug="' + CSS.escape(pre) + '"]');
      if (box) box.checked = true;
    }

    var status = document.getElementById("form-status");
    var show = function (kind, msg) {
      status.className = "form-status show " + kind;
      status.textContent = msg;
      status.focus();
    };
    var configured = form.action.indexOf("YOUR_FORM_ID") === -1;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!configured) {
        show("err", "This form isn't connected yet (Formspree ID missing). Please check back soon.");
        return;
      }
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      var label = btn.innerHTML;
      btn.textContent = "Sending…";

      var data = new FormData(form);
      var services = data.getAll("services");
      data.delete("services");
      data.append("services", services.join(", ") || "Not sure yet");

      fetch(form.action, { method: "POST", body: data, headers: { Accept: "application/json" } })
        .then(function (r) {
          if (r.ok) {
            form.reset();
            show("ok", "Thanks, your request is in. We'll reply by email to set up a scoping call.");
          } else {
            return r.json().then(function (j) {
              var m = j && j.errors ? j.errors.map(function (x) { return x.message; }).join(" ") : "";
              show("err", "Something went wrong sending the form. " + m);
            });
          }
        })
        .catch(function () { show("err", "Network error. Please try again in a moment."); })
        .finally(function () { btn.disabled = false; btn.innerHTML = label; });
    });
  }
})();
