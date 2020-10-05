$(function () {
    $('button.mark-complete').on('click', function () {
        let id = $(this).parent().attr('data-task-id');
        $.ajax({
            method: "PATCH",
            url: "/complete_item/" + id
        }).done(function( msg ) {
            location.reload();
        });
    })

    $('button.remove-task').on('click', function () {
        let id = $(this).parent().attr('data-task-id');
        $.ajax({
            method: "DELETE",
            url: "/tasks/" + id
        }).done(function( msg ) {
            location.reload();
        });
    })

    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        startDate: '+0d'
    });
})