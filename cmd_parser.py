
    def file_output(self, current_df):
        save_name = ''
        while len(save_name) == 0:
            save_name = input('\n\tSave file as: ')
        save_path = 'results/' + time.strftime('%d_%m_%Y') + '/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file_path = save_path + save_name + '.csv'
        current_df.to_csv(file_path)

    def search_keyword(self, df, chosen_column, search_term, total_length):
        # Return all rows with term in specified column
        row_index = -1
        row_list = []
        search_results = 0
        for row in df[chosen_column]:
            row_index += 1
            if type(row) is list and ';' in row:
                row_subarray = row.split(';')
                if search_term in row_subarray:
                    search_results += 1
                    row_list.append(row_index)
            else:
                if search_term in row:
                    search_results += 1
                    row_list.append(row_index)

        output_choice = ' '
        print('\tShow output (Y/N)?')
        while len(output_choice) == 0 or output_choice[0].lower() not in ('y', 'n'):
            output_choice = input('\t > ')
            if output_choice[0].lower() == 'y':
                if search_results > 0:
                    for index in row_list:
                        print('\n\n---------------------Row index:', index, '---------------')
                        print(df.irow(index))
                    print('\n\n[', search_results, 'results found for '' + search_term + '' in '' + chosen_column + '' ]')
                    # print('\tIndices:', row_list)
                else:
                    print('\n\n[ No results found for '' + search_term + '' in '' + chosen_column + '']')
            elif output_choice[0].lower() == 'n':
                break

        searched_data = []
        for index in row_list:
            searched_data.append(df.irow(index))
        new_df = pd.DataFrame(data=searched_data)

        graph = ' '
        print('\n\tCreate pie-chart with collected data (Y/N)?')
        while len(graph) == 0 or graph[0].lower() not in ('y', 'n'):
            graph = input('\t > ')
            if len(graph) > 0:
                if graph[0].lower() == 'y':
                    self.create_graph(search_results, total_length)
                elif graph[0].lower() == 'n':
                    break

        refine = ' '
        print('\n\t[S]ave this data or [R]efine?')
        while len(refine) == 0 or refine[0].lower() not in ('s', 'r'):
            refine = input('\t > ')
            if len(refine) > 0:
                if refine[0].lower() == 's':
                    self.file_output(new_df)
                elif refine[0].lower() == 'r':
                    new_column = self.pick_column(new_df)
                    new_t = self.term_prompt()
                    self.search_keyword(new_df, new_column, new_t, total_length)
        print('\n-------------------------')
