if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js', {scope: '/../'}).then(function(reg) {
        console.log('sw registrado');
    }).catch(function(error){
        console.log('sw no registrado');

  });
}
