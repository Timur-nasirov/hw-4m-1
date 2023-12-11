/* Theme Scripts */

(function ($) {
    "use strict";

    $(window).load('body', function () {
        setTimeout(function () {
            $('.site-preloader-wrap').addClass('loaded');
        }, 1000);

    });

    $(document).ready(function () {
        /*=========================================================================
            Sticky Header
        =========================================================================*/
        $(function () {
            var header = $("#header"),
                yOffset = 0,
                triggerPoint = 80;
            $(window).on('scroll', function () {
                yOffset = $(window).scrollTop();

                if (yOffset >= triggerPoint) {
                    header.addClass("navbar-fixed-top");
                } else {
                    header.removeClass("navbar-fixed-top");
                }

            });
        });

        /*=========================================================================
                Mobile Menu
        =========================================================================*/
        $('.menu-wrap ul.nav').slicknav({
            prependTo: '.header-section .navbar',
            label: '',
            allowParentLinks: true,
            closeOnClick: true
        });

        /*=========================================================================
            Testimonial Carousel
        =========================================================================*/
        $('#testimonial-carousel').owlCarousel({
            loop: true,
            margin: 25,
            autoplay: true,
            smartSpeed: 800,
            nav: true,
            navText: ['<i class="ti-angle-left"></i>', '<i class="ti-angle-right"></i>'],
            dots: false,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1,
                },
                768: {
                    items: 1,
                },
                992: {
                    items: 1,
                }
            }
        });

        /*=========================================================================
            Portfolio
        =========================================================================*/
        $('.work-items').imagesLoaded(function () {

            // Add isotope click function
            $('.work-filter li').on('click', function () {
                $(".work-filter li").removeClass("active");
                $(this).addClass("active");

                var selector = $(this).attr('data-filter');
                $(".work-items").isotope({
                    filter: selector,
                    animationOptions: {
                        duration: 750,
                        easing: 'linear',
                        queue: false,
                    }
                });
                return false;
            });

            $(".work-items").isotope({
                itemSelector: '.single-item',
                layoutMode: 'masonry',
            });
        });

        $('.work-items .work-box').each(function () {
            $(this).on('mouseenter', function () {
                if ($(this).data('title')) {
                    $('.work-titles').html($(this).data('title') + '<span class="work__cat">' + $(this).data('category') + '</span>');
                    $('.work-titles').addClass('visible');
                }

                $(document).on('mousemove', function (e) {
                    $('.work-titles').css({
                        left: e.clientX - 10,
                        top: e.clientY + 25
                    });
                });
            }).on('mouseleave', function () {
                $('.work-titles').removeClass('visible');
            });
        });

        /*=========================================================================
                Active venobox
        =========================================================================*/
        $('.img-popup').venobox({
            numeratio: true,
            infinigall: true
        });

        /*=========================================================================
            Counter Up Active
        =========================================================================*/
        var counterSelector = $('.counter');
        counterSelector.counterUp({
            delay: 10,
            time: 1000
        });

        /*=========================================================================
            Initialize smoothscroll plugin
        =========================================================================*/
        smoothScroll.init({
            offset: 60
        });

        /*=========================================================================
            Scroll To Top
        =========================================================================*/
        $(window).on('scroll', function () {
            if ($(this).scrollTop() > 100) {
                $('#scroll-to-top').fadeIn();
            } else {
                $('#scroll-to-top').fadeOut();
            }
        });

        /*=========================================================================
            WOW Active
        =========================================================================*/
        new WOW().init();

        // Current Year
        var currentYear = new Date().getFullYear();
        $('#year').append(currentYear);
    });

})(jQuery);
