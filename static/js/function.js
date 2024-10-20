$(document).ready(function () {
  $(".filter-checkbox").on("click", function () {
    console.log('a check box clicked');
    let filter_object = {};
    $(".filter-checkbox").each(function (index) {
      let filter_value = $(this).val();
      let filter_key = $(this).data("filter");
      console.log(filter_value, filter_key);
      filter_object[filter_key] = Array.from(
        document.querySelectorAll(
          "input[data-filter=" + filter_key + "]:checked"
        )
      ).map(function (element) {
        return element.value;
      });
    });
    console.log(filter_object);
  });
});
