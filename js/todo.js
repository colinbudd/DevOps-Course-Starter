$(function () {
    // Mark complete button
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

    // Remove todo item button
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