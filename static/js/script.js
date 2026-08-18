(function($) {
	
	"use strict";
	
	//Hide Loading Box (Preloader)
	function handlePreloader() {
		if($('.preloader').length){
			$('.preloader').delay(200).fadeOut(500);
		}
	}
	
	//Update Header Style and Scroll to Top
	function headerStyle() {
		if($('.main-header').length){
			var windowpos = $(window).scrollTop();
			var siteHeader = $('.main-header');
			var scrollLink = $('.scroll-to-top');
			if (windowpos >= 250) {
				siteHeader.addClass('fixed-header');
				scrollLink.fadeIn(300);
			} else {
				siteHeader.removeClass('fixed-header');
				scrollLink.fadeOut(300);
			}
		}
	}
	
	headerStyle();
	
	
	//Submenu Dropdown Toggle
	if($('.main-header li.dropdown ul').length){
		$('.main-header li.dropdown').append('<div class="dropdown-btn"><span class="fa fa-angle-down"></span></div>');
		
		//Dropdown Button
		$('.main-header li.dropdown .dropdown-btn').on('click', function() {
			$(this).prev('ul').slideToggle(500);
		});
		
		//Disable dropdown parent link
		$('.navigation li.dropdown > a').on('click', function(e) {
			e.preventDefault();
		});
	}
	
	
	//Fact Counter + Text Count
	if($('.count-box').length){
		$('.count-box').appear(function(){
	
			var $t = $(this),
				n = $t.find(".count-text").attr("data-stop"),
				r = parseInt($t.find(".count-text").attr("data-speed"), 10);
				
			if (!$t.hasClass("counted")) {
				$t.addClass("counted");
				$({
					countNum: $t.find(".count-text").text()
				}).animate({
					countNum: n
				}, {
					duration: r,
					easing: "linear",
					step: function() {
						$t.find(".count-text").text(Math.floor(this.countNum));
					},
					complete: function() {
						$t.find(".count-text").text(this.countNum);
					}
				});
			}
			
		},{accY: 0});
	}
	
	
	//Gallery With Filters
	if($('.filter-list').length){
		$('.filter-list').mixItUp({});
	}
	
	
	//Two Item Carousel
	if ($('.two-item-carousel').length) {
		$('.two-item-carousel').owlCarousel({
			loop:true,
			rtl:true,
			margin:50,
			nav:true,
			smartSpeed: 700,
			autoplay: 5000,
			navText: [ '<span class="fa fa-angle-right"></span>', '<span class="fa fa-angle-left"></span>' ],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:1
				},
				800:{
					items:2
				},
				1024:{
					items:2
				},
				1200:{
					items:2
				}
			}
		});    		
	}


	//Three Item Carousel
	if ($('.three-item-carousel').length) {
		$('.three-item-carousel').owlCarousel({
			loop:true,
			rtl:true,
			margin:50,
			nav:true,
			smartSpeed: 700,
			autoplay: 5000,
			navText: [ '<span class="fa fa-angle-right"></span>', '<span class="fa fa-angle-left"></span>' ],
			responsive:{
				0:{
					items:1
				},
				500:{
					items:1
				},
				600:{
					items:2
				},
				800:{
					items:2
				},
				1024:{
					items:3,
					margin:30,
				},
				1200:{
					items:3
				}
			}
		});    		
	}
	
	
	//Four Item Carousel
if ($('.four-item-carousel').length) {
    $('.four-item-carousel').each(function() {
        var $this = $(this);
        var isNoLoop = $this.hasClass('owl-noloop');

        $this.owlCarousel({
            loop: !isNoLoop,
            rtl:true,
            margin:0,
            nav:true,
            smartSpeed: 700,
            autoplay: 5000,
            navText: [ '<span class="fa fa-angle-right"></span>', '<span class="fa fa-angle-left"></span>' ],
            responsive:{
                0:{ items:1 },
                600:{ items:2 },
                800:{ items:3 },
                1024:{ items:4 },
                1200:{ items:4 }
            }
        });
    });
}
	
	
	// Sponsors Carousel
	if ($('.sponsors-carousel').length) {
		$('.sponsors-carousel').owlCarousel({
			loop:true,
			rtl:true,
			margin:20,
			nav:true,
			smartSpeed: 500,
			autoplay: 4000,
			navText: [ '<span class="fa fa-angle-right"></span>', '<span class="fa fa-angle-left"></span>' ],
			responsive:{
				0:{
					items:1
				},
				480:{
					items:2
				},
				600:{
					items:3
				},
				800:{
					items:4
				},
				1024:{
					items:5
				}
			}
		});    		
	}
	
	
	//Price Range Slider
	if($('.price-range-slider').length){
		$( ".price-range-slider" ).slider({
			range: true,
			min: 0,
			max: 1000000,
			values: [ 160000, 500000 ],
			slide: function( event, ui ) {
			$( "input.property-amount" ).val( ui.values[ 1 ] + " تومان - " + ui.values[ 0 ] + " تومان" );
			}
		});
		
		$( "input.property-amount" ).val( $(".price-range-slider" ).slider( "values", 1 ) + " تومان - " + $( ".price-range-slider" ).slider( "values", 0 )+ " تومان" );	
	}
	

	//Single Item Carousel
	if ($('.single-item-carousel').length) {
		$('.single-item-carousel').owlCarousel({
			loop:true,
			rtl:true,
			margin:10,
			nav:true,
			smartSpeed: 1000,
			autoplay: 5000,
			navText: [ '<span class="fa fa-angle-right"></span>', '<span class="fa fa-angle-left"></span>' ],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:1
				},
				1200:{
					items:1
				}
			}
		});    		
	}
	
	
	//Product Tabs
	if($('.project-tab').length){
		$('.project-tab .product-tab-btns .p-tab-btn').on('click', function(e) {
			e.preventDefault();
			var target = $($(this).attr('data-tab'));
			
			if ($(target).hasClass('actve-tab')){
				return false;
			}else{
				$('.project-tab .product-tab-btns .p-tab-btn').removeClass('active-btn');
				$(this).addClass('active-btn');
				$('.project-tab .p-tabs-content .p-tab').removeClass('active-tab');
				$(target).addClass('active-tab');
			}
		});
	}
	
	
	//Product Carousel
	if ($('.project-carousel').length) {
		$('.project-carousel').owlCarousel({
			loop:true,
			rtl:true,
			margin:30,
			nav:true,
			smartSpeed: 700,
			autoplay: 5000,
			navText: [ '<span class="fa fa-angle-right"></span>', '<span class="fa fa-angle-left"></span>' ],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:2
				},
				800:{
					items:2
				},
				1024:{
					items:3
				},
				1200:{
					items:4
				},
				1400:{
					items:4
				},
				1600:{
					items:4
				}
			}
		});    		
	}
	
	
	//Tabs Box
	if($('.tabs-box').length){
		$('.tabs-box .tab-buttons .tab-btn').on('click', function(e) {
			e.preventDefault();
			var target = $($(this).attr('data-tab'));
			
			if ($(target).is(':visible')){
				return false;
			}else{
				target.parents('.tabs-box').find('.tab-buttons').find('.tab-btn').removeClass('active-btn');
				$(this).addClass('active-btn');
				target.parents('.tabs-box').find('.tabs-content').find('.tab').fadeOut(0);
				target.parents('.tabs-box').find('.tabs-content').find('.tab').removeClass('active-tab');
				$(target).fadeIn(300);
				$(target).addClass('active-tab');
			}
		});
	}
	
	
	// Product Carousel Slider
	if ($('.shop-page .image-carousel').length && $('.shop-page .thumbs-carousel').length) {

		var $sync1 = $(".shop-page .image-carousel"),
			$sync2 = $(".shop-page .thumbs-carousel"),
			flag = false,
			duration = 500;

			$sync1
				.owlCarousel({
					loop:true,
					rtl:true,
					items: 1,
					margin: 0,
					nav: false,
					navText: [ '<span class="icon fa fa-angle-right"></span>', '<span class="icon fa fa-angle-left"></span>' ],
					dots: false,
					autoplay: true,
					autoplayTimeout: 5000
				})
				.on('changed.owl.carousel', function (e) {
					if (!flag) {
						flag = false;
						$sync2.trigger('to.owl.carousel', [e.item.index, duration, true]);
						flag = false;
					}
				});

			$sync2
				.owlCarousel({
					loop:true,
					rtl:true,
					margin: 10,
					items: 1,
					nav: true,
					navText: [ '<span class="icon fa fa-angle-right"></span>', '<span class="icon fa fa-angle-left"></span>' ],
					dots: false,
					center: false,
					autoplay: true,
					autoplayTimeout: 5000,
					responsive: {
						0:{
				            items:2,
				            autoWidth: false
				        },
				        400:{
				            items:3,
				            autoWidth: false
				        },
				        600:{
				            items:4,
				            autoWidth: false
				        },
				        900:{
				            items:5,
				            autoWidth: false
				        },
				        1000:{
				            items:4,
				            autoWidth: false
				        }
				    },
				})
				
		.on('click', '.owl-item', function () {
			$sync1.trigger('to.owl.carousel', [$(this).index(), duration, true]);
		})
		.on('changed.owl.carousel', function (e) {
			if (!flag) {
				flag = true;		
				$sync1.trigger('to.owl.carousel', [e.item.index, duration, true]);
				flag = false;
			}
		});

	}
	
	
	//Jquery Spinner / Quantity Spinner
	if($('.quantity-spinner').length){
		$("input.quantity-spinner").TouchSpin({
		  verticalbuttons: true
		});
	}

	
	//LightBox / Fancybox
	if($('.lightbox-image').length) {
		$('.lightbox-image').fancybox({
			openEffect  : 'fade',
			closeEffect : 'fade',
			helpers : {
				media : {}
			}
		});
	}
	
	//Contact Form Validation
	if($('#contact-form').length){

		$.extend( $.validator.messages, {
			required: "تکمیل این فیلد اجباری است.",
			remote: "لطفا این فیلد را تصحیح کنید.",
			email: "لطفا یک ایمیل صحیح وارد کنید.",
			url: "لطفا آدرس صحیح وارد کنید.",
			date: "لطفا تاریخ صحیح وارد کنید.",
			dateFA: "لطفا یک تاریخ صحیح وارد کنید.",
			dateISO: "لطفا تاریخ صحیح وارد کنید (ISO).",
			number: "لطفا عدد صحیح وارد کنید.",
			digits: "لطفا تنها رقم وارد کنید.",
			creditcard: "لطفا کریدیت کارت صحیح وارد کنید.",
			equalTo: "لطفا مقدار برابری وارد کنید.",
			extension: "لطفا مقداری وارد کنید که",
			alphanumeric: "لطفا مقدار را عدد (انگلیسی) وارد کنید.",
			maxlength: $.validator.format( "لطفا بیشتر از {0} حرف وارد نکنید." ),
			minlength: $.validator.format( "لطفا کمتر از {0} حرف وارد نکنید." ),
			rangelength: $.validator.format( "لطفا مقداری بین {0} تا {1} حرف وارد کنید." ),
			range: $.validator.format( "لطفا مقداری بین {0} تا {1} حرف وارد کنید." ),
			max: $.validator.format( "لطفا مقداری کمتر از {0} وارد کنید." ),
			min: $.validator.format( "لطفا مقداری بیشتر از {0} وارد کنید." ),
			minWords: $.validator.format( "لطفا حداقل {0} کلمه وارد کنید." ),
			maxWords: $.validator.format( "لطفا حداکثر {0} کلمه وارد کنید." )
		} );

		$('#contact-form').validate({
			rules: {
				username: {
					required: true
				},
				email: {
					required: true,
					email: true
				},
				subject: {
					required: true
				},
				message: {
					required: true
				}
			}
		});
	}
	
	// Scroll to a Specific Div
	if($('.scroll-to-target').length){
		$(".scroll-to-target").on('click', function() {
			var target = $(this).attr('data-target');
		   // animate
		   $('html, body').animate({
			   scrollTop: $(target).offset().top
			 }, 1000);
	
		});
	}
	
	// Elements Animation
	if($('.wow').length){
		var wow = new WOW(
		  {
			boxClass:     'wow',      // animated element css class (default is wow)
			animateClass: 'animated', // animation css class (default is animated)
			offset:       0,          // distance to the element when triggering the animation (default is 0)
			mobile:       false,       // trigger animations on mobile devices (default is true)
			live:         true       // act on asynchronously loaded content (default is true)
		  }
		);
		wow.init();
	}

/* ==========================================================================
   When document is Scrollig, do
   ========================================================================== */
	
	$(window).on('scroll', function() {
		headerStyle();
	});
	
/* ==========================================================================
   When document is loaded, do
   ========================================================================== */
	
	$(window).on('load', function() {
		handlePreloader();
	});	
	
/* ==========================================================================
	Custom validation messages
	========================================================================== */

	$('input[required], textarea[required]').on('invalid', function () {
		this.setCustomValidity('وارد کردن این قسمت الزامی است');
	});
	
	$('input[type="email"]').on('invalid', function () {
		if (this.validity.typeMismatch) {
			this.setCustomValidity("لطفا یک ایمیل معتبر وارد نمایید");
		}
	});
	
	$('input[required], textarea[required], input[type="email"]').on('input', function () {
		this.setCustomValidity('');
	});

})(window.jQuery);