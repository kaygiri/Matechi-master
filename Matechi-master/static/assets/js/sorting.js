page_num = 1;
// The first part is getting the price and setting the ranges
$.ajax({
  url : '',
  type : 'get',
  data : {
  text : 'price-range'
  },
  success: function(data){
    glob_price_range = data
    sessionStorage.setItem('glob_data',JSON.stringify(data))
    glob_data = sessionStorage.getItem('glob_data') 
    //glob_data = glob_price_range
    glob_data = JSON.parse(glob_data) 

    let min_price = parseInt(glob_data['min_price'])
    let max_price = parseInt(glob_data['max_price'])

    // Slider For category pages / filter price
    if ( typeof noUiSlider === 'object' ) {
    var priceSlider  = document.getElementById('price-slider');

    // Check if #price-slider elem is exists if not return
    // to prevent error logs
    //if (priceSlider == null) return;

    noUiSlider.create(priceSlider, {
    start: [ min_price,max_price ],
    connect: true,
    step: 50,
    margin: 200,
    range: {
      'min': min_price,
      'max': max_price
    },
    tooltips: true,
    format: wNumb({
          decimals: 0,
          prefix: 'NPR '
      })
    });

    console.log(priceSlider.noUiSlider.get())

    // Update Price Range
    priceSlider.noUiSlider.on('update', function( values, handle ){
    $('#filter-price-range').text(values.join(' - '));
    });
    }

    // Setting onclick listener to the page numbers
    page_link = document.getElementsByClassName('page-number');
    for(var i = 0; i < page_link.length; i++) {
      (function(index) {
        page_link[index].addEventListener("click", function() {
          page_num = index+1;
          console.log('asdfads',+page_num);
          sessionStorage.setItem('current_page', JSON.stringify(page_num));
          submit_query_params();
        })
      })(i);
    }

    // Setting on click listeners to Next and Previous page numbers
    next_btn = document.getElementById('next-button');
    previous_btn = document.getElementById('previous-button');
    if (next_btn!= null)
    {
      next_btn.addEventListener('click',function(){
      current_page = JSON.parse(sessionStorage.getItem('current_page'));
      page_num = current_page + 1;
      sessionStorage.setItem('current_page', JSON.stringify(page_num));
      submit_query_params();
      })
    }
    if (previous_btn!= null)
      {
        previous_btn.addEventListener('click',function(){
        current_page = JSON.parse(sessionStorage.getItem('current_page'));
        page_num = current_page - 1;
        sessionStorage.setItem('current_page', JSON.stringify(page_num));
        submit_query_params();
        })   
    }

    // when loaded retain values
    window.onload = on_reload_do();

    function on_reload_do(){
        //cat_list = sessionStorage.getItem('cat_list');
        //console.log(cat_list);

        cat_list = JSON.parse(sessionStorage.getItem('cat_list'));
          
        // This is for sidebar filtering
        var userSelection = document.getElementsByClassName('custom-control-input');

        if (cat_list !=null)
        {
          for (j=0;j<cat_list.length;j++){
            console.log(cat_list[j]);
            for (i=0; i<userSelection.length;i++)
            {
              if (cat_list[j]==userSelection[i].value)
              {
                userSelection[i].checked = true;
              }
            }
          }



        pr = sessionStorage.getItem('selected_price');
        pr = JSON.parse(pr)
        priceSlider.noUiSlider.set([pr[0],pr[1]]);

        }



        // retain values for sorting dropdown
        selected_val =sessionStorage.getItem('selected_value');
        console.log(selected_val);

        var select = document.getElementById('sortby');
        var option;

        for (var i=0; i<select.options.length; i++) 
        {
        option = select.options[i];

        if (option.value == selected_val) 
        {
            option.setAttribute('selected', true);
            // For a single select, the job's done
            return; 
        } 
        }
      }

    function submit_query_params(){
      base_url = '?';
      category_list = get_category_params();

      for (i=0;i<category_list.length;i++)
      {
        if (i==0)
        {
          base_url = base_url+'category=' + category_list[i];
        }
        else
        {
          base_url = base_url+'&category=' + category_list[i];
        }
      }
      
      // Create sort parameters
      sort_value = get_sort_params();
      base_url = base_url + '&sort_by=' + sort_value;
      console.log(base_url);

      // price range params
      // Retain price range
      values = priceSlider.noUiSlider.get()
      sessionStorage.setItem('selected_price',JSON.stringify(values))

      base_url = base_url + '&min_price=' + values[0]
      base_url = base_url + '&max_price=' + values[1]

      // Create page parameters
      //alert('current' + page_num);
      base_url = base_url + '&page=' + page_num;

      window.location = base_url;
    }

    var get_category_params = ()=>{
      var cat_list =[]
      for (i=0; i<userSelection.length; i++)
      {
        if (userSelection[i].checked == true)
        {
        cat_list.push(userSelection[i].value);
        }
      }
      sessionStorage.setItem('cat_list',JSON.stringify(cat_list));
      return cat_list;
    }

    var get_sort_params = ()=>{
      var sort = document.getElementById('sortby');
      sessionStorage.setItem('selected_value',sort.value);
      return sort.value;
    }

    // This is just dropdown sorting
    document.getElementById('sortby').onchange = function(){
      submit_query_params();
        //submit_sorting_values();
    };

    function submit_sorting_values() {
        var sort = document.getElementById('sortby');
        //alert(sort.value);

        sessionStorage.setItem('selected_value',sort.value);
        var sort_form = document.getElementById('sorting');
        sort_form.submit();
    }

    // This is for sidebar filtering
    var userSelection = document.getElementsByClassName('custom-control-input');



    /*for(var i = 0; i < userSelection.length; i++) {
      (function(index) {
        count = i+1;
        var idmaker = 'label-' + count.toString();
        var formidmaker = 'category-filter-form-' + count.toString();
        //alert(idmaker);
        userSelection[index].addEventListener("change", function() {
          var lb = document.getElementById(idmaker).textContent;
          alert(lb);

          // Get the form and submit
          document.getElementById(formidmaker).submit();
        })
      })(i);
    }*/

    /*for(var i = 0; i < userSelection.length; i++) {
      (function(index) {

        //get the array in sessionstorage 
        cat_list = {}

        // make dynamic ids
        count = i+1;
        var idmaker = 'label-' + count.toString();
        var formidmaker = 'category-filter-form-' + count.toString();

        // onchange do this
        userSelection[index].addEventListener("change", function() {
          us_bool = userSelection[index].checked;

          // if the box is checked
          if (us_bool == true) {
            // update JSON
            var lb = document.getElementById(idmaker).textContent;
            alert(lb);
            
            // JSON add
            cat_list[lb] = lb;
            console.log(cat_list);

            // Save it in Session Storage
            sessionStorage.setItem('cat_list',JSON.stringify(cat_list));
            make_ajax_call();
          }

          // if unchecked then remove
          if (us_bool == false)
          {
            var lb = document.getElementById(idmaker).textContent;
            alert(lb)

            console.log('deleting' + cat_list[lb])

            delete cat_list[lb];

            sessionStorage.setItem('cat_list',JSON.stringify(cat_list))

            console.log(cat_list);
            make_ajax_call();
          }

          // Get the form and submit
          //document.getElementById(formidmaker).submit();
        })
      })(i);
    }

    make_ajax_call = ()=>{
      $(document).ready(function(){
        $.ajax({
          url:'',
          dataType:'json',
          type:'get',
          data: {
            category_list :sessionStorage.getItem('cat_list')
          },
          success : function(response){
            //alert('succesful get request !!!!');
          },

        })
      });
    }*/

    // retain filter values
    document.getElementById('clear-btn').addEventListener('click', function(e){
      e.preventDefault();
      sessionStorage.clear();
      window.location = window.location.pathname
    })



    document.getElementById('submit-filters').addEventListener('click', submit_query_params);

    function retain_category_filter(){
      var cat_list =[]
      for (i=0; i<userSelection.length; i++)
      {
        if (userSelection[i].checked == true)
        {
        cat_list.push(userSelection[i].value);
        }
      }
      sessionStorage.setItem('cat_list',JSON.stringify(cat_list));
    }



      },
      error: function(){
          alert("error");
      }
    });

