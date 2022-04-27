document.getElementById('invoice-print').addEventListener('click', function(e){
    window.print();
})

document.getElementById('download-pdf').addEventListener('click', function(e){
    var invoice = document.getElementById("invoice");

    file_name = document.getElementById('download-pdf').getAttribute('data-filename');
    file_name = 'Invoice' + '-' + file_name + '.pdf';

    var opt = {
        filename: file_name,
        image: { type: 'jpeg', quality: 0.98 },
    };
    html2pdf().from(invoice).set(opt).save();
})                                                                                  