if (location.pathname.replace(/\/$/, '') === '/privacy' && ['#qr-policy', '#qr-scanner'].includes(location.hash)) location.replace('/apps/qr-scanner/privacy/');
document.querySelectorAll('.navbar nav a').forEach(link => {
 const current = location.pathname;
 const href = link.getAttribute('href');
 if (current === href || (href !== '/' && current.startsWith(href))) link.setAttribute('aria-current', 'page');
});
