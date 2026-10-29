(function () {
  "use strict";
  var D = document, W = window, reduce = W.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hero = D.querySelector(".hero");
  requestAnimationFrame(function () { requestAnimationFrame(function () { hero && hero.classList.add("go-in"); }); });

  // revelação com escalonamento
  D.querySelectorAll(".stats li,.svc li,.timeline li").forEach(function (el, i) {
    el.style.setProperty("--d", (Array.prototype.indexOf.call(el.parentNode.children, el) % 4) * 0.08 + "s");
  });
  var els = D.querySelectorAll(".rv");
  if (reduce || !("IntersectionObserver" in W)) els.forEach(function (el) { el.classList.add("in"); });
  else {
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); count(x.target); } });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.1 });
    els.forEach(function (el) { io.observe(el); });
  }

  // contadores
  function count(root) {
    var el = root.querySelector && root.querySelector("[data-count]");
    if (!el || reduce) return;
    var end = +el.getAttribute("data-count"), t0 = null;
    el.textContent = "0";
    requestAnimationFrame(function step(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / 1500, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 4)));
      if (p < 1) requestAnimationFrame(step);
    });
  }

  // header + parallax do retrato e dos prints
  var top = D.querySelector(".top"), portrait = D.querySelector(".portrait img"), shots = D.querySelectorAll(".shot img"), tick = false;
  function frame() {
    tick = false;
    var y = W.scrollY;
    top.classList.toggle("on", y > 30);
    if (reduce) return;
    if (portrait && y < W.innerHeight) portrait.style.transform = "translate3d(0," + y * 0.14 + "px,0)";
    var vh = W.innerHeight;
    shots.forEach(function (img) {
      var r = img.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      var p = (r.top + r.height / 2 - vh / 2) / vh;
      img.style.objectPosition = "50% " + (50 + p * 18) + "%";
    });
  }
  W.addEventListener("scroll", function () { if (!tick) { tick = true; requestAnimationFrame(frame); } }, { passive: true });
  frame();

  // botões magnéticos (desktop)
  if (!reduce && W.matchMedia("(hover:hover)").matches) {
    D.querySelectorAll(".magnet").forEach(function (b) {
      b.addEventListener("pointermove", function (e) {
        var r = b.getBoundingClientRect();
        b.style.transform = "translate(" + (e.clientX - r.left - r.width / 2) * 0.18 + "px," + (e.clientY - r.top - r.height / 2) * 0.28 + "px)";
      });
      b.addEventListener("pointerleave", function () { b.style.transition = "transform .5s cubic-bezier(.16,.84,.24,1)"; b.style.transform = ""; setTimeout(function () { b.style.transition = ""; }, 500); });
    });
  }
})();
