(function(){const toggleSideBarButton=document.getElementById('toggleSidebarMobile');const parentElement=document.getElementById('sidebar');let showSidebar=true;function toggleSideBarDisplay(){const spans=parentElement.querySelectorAll('a span');if(showSidebar){spans.forEach(span=>{span.classList.add('hidden');});parentElement.classList.add('w-40');showSidebar=false;return}
spans.forEach(span=>{span.classList.remove('hidden');});parentElement.classList.remove('w-16');showSidebar=true;}
toggleSideBarButton.addEventListener('click',()=>{toggleSideBarDisplay();})})();