$(function () {
    $('button.mark-complete').on('click', function () {
        let id = $(this).parent().attr('data-task-id');
        $.ajax({
            method: "PUT",
            url: "/tasks/" + id,
            data: { action: "mark_complete" }
        }).done(function( msg ) {
            location.reload();
        });
    })
})