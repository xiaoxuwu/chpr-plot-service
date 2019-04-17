def validate_new_plot_metadata(request):
    if not request.POST['name']:
        return (False, 'Plot name cannot be empty.')
    if not request.FILES['raw_data'] or request.FILES['raw_data'].content_type != 'text/csv':
        return (False, 'Please upload a csv file.')
    if not request.POST['data_type']:
        return (False, 'Please select a data type.')
    return (True, 'Success')