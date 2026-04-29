import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Smooth scroll
if 'scroll-behavior: smooth' not in text:
    text = text.replace('<style>', '<style>\n        html { scroll-behavior: smooth; }')

# IDs
text = text.replace('<main class="container mx-auto px-4 pb-12">', '<main id="accueil" class="container mx-auto px-4 pt-10 pb-12 -mt-10">')
text = text.replace('<!-- About Us Section -->\n    <section class="container mx-auto px-4 py-8 mb-12">', '<!-- About Us Section -->\n    <section id="apropos" class="container mx-auto px-4 pt-16 pb-8 mb-12 -mt-8">')
text = text.replace('<!-- Benefits Section -->\n    <section class="container mx-auto px-4 py-16 mb-12">', '<!-- Benefits Section -->\n    <section id="fonctionnalites" class="container mx-auto px-4 pt-20 pb-16 mb-12 -mt-4">')
text = text.replace('<!-- Open Positions Section -->\n    <section class="container mx-auto px-4 py-16 mb-12">', '<!-- Open Positions Section -->\n    <section id="offres" class="container mx-auto px-4 pt-20 pb-16 mb-12 -mt-4">')
text = text.replace('<!-- CTA Section -->\n    <section class="container mx-auto px-4 py-8 mb-16">', '<!-- CTA Section -->\n    <section id="contact" class="container mx-auto px-4 pt-20 pb-8 mb-16 -mt-12">')
text = text.replace('<!-- Testimonials Section -->\n    <section class="container mx-auto px-4 py-16 mb-16">', '<!-- Testimonials Section -->\n    <section id="temoignages" class="container mx-auto px-4 pt-20 pb-16 mb-16 -mt-4">')

# Header Links
text = text.replace('<a href="#" class="hover:text-[#08265c] transition-colors">Accueil</a>', '<a href="#accueil" class="hover:text-[#08265c] font-bold text-[#08265c] transition-colors">Accueil</a>')
text = text.replace('<a href="#" class="hover:text-[#08265c] transition-colors">À propos</a>', '<a href="#apropos" class="hover:text-[#08265c] transition-colors">À propos</a>')
text = text.replace('<a href="#" class="hover:text-[#08265c] transition-colors">Offres d\'emploi</a>', '<a href="#offres" class="hover:text-[#08265c] transition-colors">Offres d\'emploi</a>')
text = text.replace('<a href="#" class="hover:text-[#08265c] transition-colors">Fonctionnalités</a>', '<a href="#fonctionnalites" class="hover:text-[#08265c] transition-colors">Fonctionnalités</a>')
text = text.replace('<a href="#" class="hover:text-[#08265c] transition-colors">Contact</a>', '<a href="#contact" class="hover:text-[#08265c] transition-colors">Contact</a>')
text = text.replace('<a href="#" class="hover:text-[#08265c] transition-colors">Témoignages</a>', '<a href="#temoignages" class="hover:text-[#08265c] transition-colors">Témoignages</a>')

# Add mobile menu and burger icon
mobile_menu = """        <!-- Burger Icon -->
        <button id="mobile-menu-btn" class="md:hidden text-gray-700 hover:text-[#08265c] focus:outline-none z-50 relative">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
        </button>

        <!-- CTA Button -->"""

if "mobile-menu-btn" not in text:
    text = text.replace('<!-- CTA Button -->', mobile_menu)

mobile_nav_panel = """    </header>

    <!-- Mobile Nav Panel -->
    <div id="mobile-nav" class="fixed inset-0 bg-white z-40 transform translate-x-full transition-transform duration-300 ease-in-out md:hidden flex flex-col pt-24 px-8 pb-8 shadow-2xl">
        <nav class="flex flex-col gap-6 text-xl font-bold text-gray-800">
            <a href="#accueil" class="mobile-link hover:text-[#3f8a3e] border-b border-gray-100 pb-2">Accueil</a>
            <a href="#apropos" class="mobile-link hover:text-[#3f8a3e] border-b border-gray-100 pb-2">À propos</a>
            <a href="#offres" class="mobile-link hover:text-[#3f8a3e] border-b border-gray-100 pb-2">Offres d'emploi</a>
            <a href="#fonctionnalites" class="mobile-link hover:text-[#3f8a3e] border-b border-gray-100 pb-2">Fonctionnalités</a>
            <a href="#contact" class="mobile-link hover:text-[#3f8a3e] border-b border-gray-100 pb-2">Contact</a>
            <a href="#temoignages" class="mobile-link hover:text-[#3f8a3e] border-b border-gray-100 pb-2">Témoignages</a>
        </nav>
        <div class="mt-auto">
            <a href="#contact" class="mobile-link block text-center bg-[#3f8a3e] hover:bg-[#2e682d] text-white px-6 py-4 rounded-xl font-bold transition-colors shadow-lg shadow-green-200">
                Postuler maintenant
            </a>
        </div>
    </div>

    <!-- Hero Section -->"""

if "mobile-nav" not in text:
    text = text.replace('</header>\n\n    <!-- Hero Section -->', mobile_nav_panel)

# Mobile JS logic
js_logic = """<script>
        // Mobile Menu Toggle
        const mobileBtn = document.getElementById('mobile-menu-btn');
        const mobileNav = document.getElementById('mobile-nav');
        const mobileLinks = document.querySelectorAll('.mobile-link');
        let menuOpen = false;

        mobileBtn.addEventListener('click', () => {
            menuOpen = !menuOpen;
            if (menuOpen) {
                mobileNav.classList.remove('translate-x-full');
                mobileBtn.innerHTML = `<svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>`;
            } else {
                mobileNav.classList.add('translate-x-full');
                mobileBtn.innerHTML = `<svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>`;
            }
        });

        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuOpen = false;
                mobileNav.classList.add('translate-x-full');
                mobileBtn.innerHTML = `<svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>`;
            });
        });"""

if "Mobile Menu Toggle" not in text:
    text = text.replace('<script>', js_logic)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
