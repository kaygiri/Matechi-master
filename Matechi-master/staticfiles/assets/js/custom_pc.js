localStorage.clear();
var submit = true;
var counter = 1;
var fotorama;
var $fotoramaDiv;
var total;

var set_image = ()=>{
    // Initialize fotoroma exactly once manually
    if (counter == 1)
    {
    $fotoramaDiv = $('#fotorama-carousel').fotorama();
    }

    // Render the case images in the left at the start, also whenever new case is selected
    var cpu_case = document.getElementsByClassName('case-selected');

    thumbnail = (cpu_case[0].dataset.thumbnail);
    var product_name = cpu_case[0].textContent;
    case_name1 = cpu_case[0].getAttribute('data-name');
    document.getElementById('case-name').textContent = case_name1;

    // 2. Get the API object.
    fotorama = $fotoramaDiv.data('fotorama');

    fotorama.load([
        {img: thumbnail, thumb: thumbnail}
        ]);

    // Get the other images slowly and push it to the stack    

    loop_counter = cpu_case[0].dataset.loopcounter;
    for (let j = 1; j <= loop_counter; j++)
    { 
        name1 = 'data-' + j.toString();
        image_url = cpu_case[0].getAttribute(name1);
        console.log('ssss', image_url);

        fotorama.push(
            {img: image_url, thumb: image_url}
            );
    }



    // Set the case heading
    var carousel = document.getElementById('fotorama-carousel');


        }

set_image();

update_image = (value)=>{
    var cpu_case = document.getElementsByClassName('case-selected');
    cpu_case[0].classList.remove('case-selected');

    var cpu_case2 = document.getElementsByClassName('case-select');

    for (i=0; i<cpu_case2.length; i++)
    {
        console.log(cpu_case2[i].textContent)
        if (cpu_case2[i].textContent == value)
        {
            cpu_case2[i].classList.add('case-selected');
        }
    }
    counter = counter+1;
    set_image();

}        


var sel_case = document.getElementById('inputcase');

sel_case.addEventListener('change', function(){
    update_image(sel_case.value);
})


// Render dynamic price

calculate_total = ()=>{
    var total = 0;
    // Calculate processor
    sel = document.getElementById('inputProcessor');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    total = total + parseInt(price);

    // Calculate motherboard
    sel = document.getElementById('inputmb');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    total = total + parseInt(price);

    // Calculate graphics
    sel = document.getElementById('inputgraphics');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    total = total + parseInt(price);

    // Calculate ram
    sel = document.getElementById('inputram');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');

    sel = document.getElementById('inputqty1');
    option = sel.options[sel.selectedIndex];
    qty = option.getAttribute('data-qty');
    price = parseInt(price) * parseInt(qty);


    total = total + parseInt(price);

    // Calculate primary storage
    sel = document.getElementById('inputps');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    total = total + parseInt(price);

    // Calculate secondary storage
    sel = document.getElementById('inputss');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');

    sel = document.getElementById('inputqty2');
    option = sel.options[sel.selectedIndex];
    qty = option.getAttribute('data-qty');
    price = parseInt(price) * parseInt(qty);

    total = total + parseInt(price);

    // Calculate processor
    sel = document.getElementById('inputcase');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    total = total + parseInt(price);

    // Calculate cpu cooler
    sel = document.getElementById('inputcooler');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    total = total + parseInt(price);

    // Calculate PSU
    sel = document.getElementById('inputpsu');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    total = total + parseInt(price);

    document.getElementById('total-price').textContent = total;
}

calculate_total();


document.getElementById('submit').addEventListener('click', function(){
    calculate_total();
})

// While each form is changed render total
my_options = document.getElementsByClassName('my-form');
for(i=0; i<my_options.length; i++)
{
    my_options[i].addEventListener('change', function(){
        calculate_total();
    })
}

validate_form = ()=>{
    var total = 0;
    // Calculate processor
    sel = document.getElementById('inputProcessor');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    if (parseInt(price) == 0)
    {
        submit = false;
    }

    total = total + parseInt(price);

    // Calculate motherboard
    sel = document.getElementById('inputmb');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    if (parseInt(price) == 0)
    {
        submit = false;
    }
    total = total + parseInt(price);

    // Calculate graphics
    sel = document.getElementById('inputgraphics');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    if (parseInt(price) == 0)
    {
        submit = false;
    }

    total = total + parseInt(price);

    // Calculate ram
    sel = document.getElementById('inputram');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    if (parseInt(price) == 0)
    {
        submit = false;
    }


    sel = document.getElementById('inputqty1');
    option = sel.options[sel.selectedIndex];
    qty = option.getAttribute('data-qty');
    price = parseInt(price) * parseInt(qty);


    total = total + parseInt(price);

    // Calculate primary storage
    sel = document.getElementById('inputps');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    if (parseInt(price) == 0)
    {
        submit = false;
    }

    total = total + parseInt(price);

    // Calculate secondary storage
    sel = document.getElementById('inputss');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    if (parseInt(price) == 0)
    {
        submit = false;
    }
   

    sel = document.getElementById('inputqty2');
    option = sel.options[sel.selectedIndex];
    qty = option.getAttribute('data-qty');
    price = parseInt(price) * parseInt(qty);

    total = total + parseInt(price);

    // Calculate CPU case
    sel = document.getElementById('inputcase');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    if (parseInt(price) == 0)
    {
        submit = false;
    }

    total = total + parseInt(price);

    // Calculate cpu cooler
    sel = document.getElementById('inputcooler');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    if (parseInt(price) == 0)
    {
        submit = false;
    }

    total = total + parseInt(price);

    // Calculate PSU
    sel = document.getElementById('inputpsu');
    option = sel.options[sel.selectedIndex];
    price = option.getAttribute('data-price');
    if (parseInt(price) == 0)
    {
        submit = false;
    }
 
    total = total + parseInt(price);

    if (submit == false)
    {
        document.getElementsByClassName('alert-empty')[0].style.display = 'block';
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    else{
        document.getElementsByClassName('alert-empty')[0].style.display = 'None'
    }

    document.getElementById('total-price').textContent = total;
    return total;
}

check_compatibility = ()=>{
        // Check processor
        sel = document.getElementById('inputProcessor');
        option = sel.options[sel.selectedIndex];
        brand1 = option.getAttribute('data-brand');

    
        // Calculate motherboard
        sel = document.getElementById('inputmb');
        option = sel.options[sel.selectedIndex];
        brand2 = option.getAttribute('data-brand');

        console.log(brand1, brand2);

        if (brand1.toLowerCase() == 'amd' || brand1.toLowerCase() == 'intel')
        {
            if (brand2.toLowerCase() == 'amd' || brand2.toLowerCase() == 'intel'){
                if (brand1 != brand2)
                {
                    document.getElementsByClassName('alert-invalid')[0].style.display = 'block';
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                    submit = false;
                }
                else{
                    document.getElementsByClassName('alert-invalid')[0].style.display = 'None';
                }
            }

        }


}


// When submit button pressed, first validate the form and then submit
document.getElementById('submit').addEventListener('click', function(e){
    submit_quotation();
})

submit_quotation = ()=>{
    total = validate_form();
    check_compatibility();
    if (submit == true)
    {
    // Save the items in the local storage and proceed to checkout
    // Calculate processor
    sel = document.getElementById('inputProcessor');
    option = sel.options[sel.selectedIndex];
    id = option.getAttribute('data-id');
    price = option.getAttribute('data-price');
    name1 = option.getAttribute('data-name');
    localStorage.setItem('processor_name', JSON.stringify(name1));
    localStorage.setItem('processor_price', JSON.stringify(price));
    localStorage.setItem('processor_id', JSON.stringify(id));

    // Calculate motherboard
    sel = document.getElementById('inputmb');
    option = sel.options[sel.selectedIndex];
    id = option.getAttribute('data-id');
    price = option.getAttribute('data-price');
    name1 = option.getAttribute('data-name');
    localStorage.setItem('motherboard_name', JSON.stringify(name1));
    localStorage.setItem('motherboard_price', JSON.stringify(price));
    localStorage.setItem('motherboard_id', JSON.stringify(id));

    // Calculate graphics
    sel = document.getElementById('inputgraphics');
    option = sel.options[sel.selectedIndex];
    id = option.getAttribute('data-id');
    price = option.getAttribute('data-price');
    name1 = option.getAttribute('data-name');
    localStorage.setItem('graphics_name', JSON.stringify(name1));
    localStorage.setItem('graphics_price', JSON.stringify(price));
    localStorage.setItem('graphics_id', JSON.stringify(id));

    // Calculate ram
    sel = document.getElementById('inputram');
    option = sel.options[sel.selectedIndex];
    id = option.getAttribute('data-id');
    price = option.getAttribute('data-price');
    name1 = option.getAttribute('data-name');
    localStorage.setItem('ram_name', JSON.stringify(name1));
    localStorage.setItem('ram_price', JSON.stringify(price));
    localStorage.setItem('ram_id', JSON.stringify(id));

    sel = document.getElementById('inputqty1');
    option = sel.options[sel.selectedIndex];
    qty = option.getAttribute('data-qty');
    localStorage.setItem('ram_quantity', JSON.stringify(qty));


    // Calculate primary storage
    sel = document.getElementById('inputps');
    option = sel.options[sel.selectedIndex];
    id = option.getAttribute('data-id');
    price = option.getAttribute('data-price');
    name1 = option.getAttribute('data-name');
    localStorage.setItem('primary_name', JSON.stringify(name1));
    localStorage.setItem('primary_price', JSON.stringify(price));
    localStorage.setItem('primary_id', JSON.stringify(id));

    // Calculate secondary storage
    sel = document.getElementById('inputss');
    option = sel.options[sel.selectedIndex];
    id = option.getAttribute('data-id');
    price = option.getAttribute('data-price');
    name1 = option.getAttribute('data-name');
    localStorage.setItem('secondary_name', JSON.stringify(name1));
    localStorage.setItem('secondary_price', JSON.stringify(price));
    localStorage.setItem('secondary_id', JSON.stringify(id));

    sel = document.getElementById('inputqty2');
    option = sel.options[sel.selectedIndex];
    qty = option.getAttribute('data-qty');
    localStorage.setItem('secondary_quantity', JSON.stringify(qty));


    // Calculate case
    sel = document.getElementById('inputcase');
    option = sel.options[sel.selectedIndex];
    id = option.getAttribute('data-id');
    price = option.getAttribute('data-price');
    name1 = option.getAttribute('data-name');
    localStorage.setItem('case_name', JSON.stringify(name1));
    localStorage.setItem('case_price', JSON.stringify(price));
    localStorage.setItem('case_id', JSON.stringify(id));

    // Calculate cpu cooler
    sel = document.getElementById('inputcooler');
    option = sel.options[sel.selectedIndex];
    id = option.getAttribute('data-id');
    price = option.getAttribute('data-price');
    name1 = option.getAttribute('data-name');
    localStorage.setItem('cooler_name', JSON.stringify(name1));
    localStorage.setItem('cooler_price', JSON.stringify(price));
    localStorage.setItem('cooler_id', JSON.stringify(id));

    // Calculate PSU
    sel = document.getElementById('inputpsu');
    option = sel.options[sel.selectedIndex];
    id = option.getAttribute('data-id');
    price = option.getAttribute('data-price');
    name1 = option.getAttribute('data-name');
    localStorage.setItem('psu_name', JSON.stringify(name1));
    localStorage.setItem('psu_price', JSON.stringify(price));
    localStorage.setItem('psu_id', JSON.stringify(id));

    localStorage.setItem('total_price', JSON.stringify(total));

    window.location.href = '/custom-pc-nepal/checkout/'

    }

}



