$(function() {
	$('#ingredient-select').selectize();
});

$(document).ready(function() {

    $('#form').validate({

        ignore: ':hidden:not([class~=selectized]),:hidden > .selectized, .selectize-control .selectize-input input',

        rules: {
            'utensils': {
                required: true
            },
            'grams': {
                required: true,
                min: 0
            },
            'ingredient': {
                required: true
            },
        },

        messages: {
            'utensils': {
                required: 'Escolha pelo menos um utensílio'
            },
            'grams': {
                required: 'Digite um valor em gramas',
                min: 'O valor deve ser positivo',
                number: 'Este campo aceita somente números'
            },
            'ingredient': {
                required: 'Escolha um ingrediente'
            },
        },

        errorPlacement: function(error, element) {
            if(element.attr("name") == "grams") {
                $('#error-grams').append(error);
            } else if(element.attr("name") == "utensils") {
                $('#error-utensils').append(error);
            } else if(element.attr("name") == "ingredient") {
                $('#error-ingredient').append(error);
            }
        }
    });

    $('#ingredient-select').on('change', function() {
        $('#ingredient-select').valid();
    });
});