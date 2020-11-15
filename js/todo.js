$(function () {
    $('button.move-list').on('click', function () {
        let id = $(this).parent().attr('data-task-id');
        let targetList = $(this).attr('data-target-list');
        $.ajax({
            method: "PATCH",
            url: "/tasks/" + id,
            data: { "targetList": targetList }
        }).done(function( msg ) {
            location.reload();
        });
    });

    $('button.remove-task').on('click', function () {
        let id = $(this).parent().attr('data-task-id');
        $.ajax({
            method: "DELETE",
            url: "/tasks/" + id
        }).done(function( msg ) {
            location.reload();
        });
    });

    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        startDate: '+0d'
    });
});