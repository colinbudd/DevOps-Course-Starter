$(function () {
    $('button.mark-complete').on('click', function () {
        let id = $(this).parent().attr('data-task-id');
        $.ajax({
            method: "PATCH",
            url: "/tasks/" + id,
            data: { action: "mark_complete" }
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
})