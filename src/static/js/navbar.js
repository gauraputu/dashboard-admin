(function(){
    const toggleSideBarButton = document.getElementById('toggleSidebarMobile');
    const parentElement = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content')
    let showSidebar = true;

    function toggleSideBarDisplay() {
        const spans = parentElement.querySelectorAll('a span');

        // show sidebar
        if (showSidebar) {
            spans.forEach(span => {
                span.classList.add('hidden');
            });
            parentElement.classList.replace('w-40','w-16');
            mainContent.classList.replace('ml-40', 'ml-16');
            showSidebar = false;
            return
        }
        // hide sidebar
        spans.forEach(span => {
            span.classList.remove('hidden');
        });
        parentElement.classList.replace('w-16', 'w-40');
        mainContent.classList.replace('ml-16', 'ml-40');
        showSidebar = true;
    }

    toggleSideBarButton.addEventListener('click', ()=>{
        toggleSideBarDisplay();
    })
})()