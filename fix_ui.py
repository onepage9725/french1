import re

with open("index.html", "r") as f:
    content = f.read()

# Fix top right card
content = content.replace(
    '''<div class="floating-card absolute top-10 right-4 lg:right-12 bg-white rounded-3xl p-6 flex flex-col items-center gap-2 z-20 w-48">''',
    '''<div class="floating-card absolute top-4 lg:top-10 right-2 lg:right-12 bg-white rounded-3xl p-4 lg:p-6 flex flex-col items-center gap-1 lg:gap-2 z-20 w-32 lg:w-48 shadow-lg scale-90 lg:scale-100 origin-top-right">'''
)
content = content.replace(
    '''<div class="w-12 h-12 bg-[#3f8a3e] rounded-full flex items-center justify-center text-white mb-1 shadow-md">''',
    '''<div class="w-8 h-8 lg:w-12 lg:h-12 bg-[#3f8a3e] rounded-full flex items-center justify-center text-white mb-1 shadow-md">'''
)
content = content.replace(
    '''<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">''',
    '''<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-4 h-4 lg:w-6 lg:h-6">'''
)
content = content.replace(
    '''<div class="text-[#08265c] font-bold text-2xl">2,638+</div>''',
    '''<div class="text-[#08265c] font-bold text-lg lg:text-2xl leading-none">2,638+</div>'''
)

# Fix left middle card
content = content.replace(
    '''<div class="floating-card delay-1 absolute top-1/2 left-0 lg:left-4 transform -translate-y-1/2 bg-white rounded-3xl p-6 flex flex-col items-start gap-1 z-20 w-44">''',
    '''<div class="floating-card delay-1 absolute top-1/2 left-0 lg:left-4 transform -translate-y-1/2 bg-white rounded-3xl p-4 lg:p-6 flex flex-col items-start gap-1 z-20 w-32 lg:w-44 shadow-lg scale-90 lg:scale-100 origin-left">'''
)
content = content.replace(
    '''<div class="text-[#08265c] font-bold text-3xl">1,618+</div>''',
    '''<div class="text-[#08265c] font-bold text-xl lg:text-3xl leading-none">1,618+</div>'''
)
content = content.replace(
    '''<div class="text-gray-500 text-sm font-semibold">Demandeurs d'emploi</div>''',
    '''<div class="text-gray-500 text-xs lg:text-sm font-semibold leading-tight">Demandeurs d'emploi</div>'''
)


# Fix bottom right card
content = content.replace(
    '''<div class="floating-card delay-2 absolute bottom-24 right-0 lg:-right-8 bg-white rounded-3xl p-6 flex flex-col gap-3 z-20 shadow-xl border border-gray-50 w-56">''',
    '''<div class="floating-card delay-2 absolute bottom-12 lg:bottom-24 right-0 lg:-right-8 bg-white rounded-3xl p-3 lg:p-6 flex flex-col gap-2 lg:gap-3 z-20 shadow-xl border border-gray-50 w-44 lg:w-56 scale-90 lg:scale-100 origin-bottom-right">'''
)
content = content.replace(
    '''<div class="flex -space-x-3">''',
    '''<div class="flex -space-x-2 lg:-space-x-3">'''
)
# We can just match the images and alter their classes
content = content.replace(
    '''class="w-10 h-10 rounded-full border-2 border-white object-cover"''',
    '''class="w-8 h-8 lg:w-10 lg:h-10 rounded-full border-2 border-white object-cover"'''
)

# Fix script binding for testimonials
script_fix = """            function nextTestimonial() {
                setTestimonial(actIdx === testimonials.length - 1 ? 0 : actIdx + 1);
            }
            
            window.prevTestimonial = prevTestimonial;
            window.nextTestimonial = nextTestimonial;
            window.setTestimonial = setTestimonial;"""
            
content = content.replace(
    """            function nextTestimonial() {
                setTestimonial(actIdx === testimonials.length - 1 ? 0 : actIdx + 1);
            }""",
    script_fix
)

with open("index.html", "w") as f:
    f.write(content)

print("Modifications done!")
