(function(){const toggleSideBarButton=document.getElementById('toggleSidebarMobile');const parentElement=document.getElementById('sidebar');let showSidebar=false;function toggleSideBarDisplay(){const spans=parentElement.querySelectorAll('a span');if(showSidebar){spans.forEach(span=>{span.classList.add('hidden');});showSidebar=false;return}
spans.forEach(span=>{span.classList.remove('hidden');});showSidebar=true;}
toggleSideBarButton.addEventListener('click',()=>{toggleSideBarDisplay();})})();