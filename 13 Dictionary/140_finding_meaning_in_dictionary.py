d1={
    'Eloquent':'Fluent or persuasive in speaking or writing.',
    'Meticulous':'Showing great attention to detail; very careful and precise in ones work, actions, or efforts.',
    'Ubiquitous ':'Present, appearing, or found everywhere. Something that is ubiquitous is very common and widespread.',
    'Ambiguous':'Open to more than one interpretation or having a double meaning.',
    'Sycophant':'A person who acts obsequiously towards someone important in order to gain advantage.'
}
list_keys=list(d1.keys())
list_values=list(d1.values())

list_len=[len(item) for item in list_values]

max_value=max(list_len)
min_value=min(list_len)

max_index=list_len.index(max_value)
min_index=list_len.index(min_value)

print(f'Maximum key is {list_keys[max_index]} and sentence is "{list_values[max_index]}"')
print('\n')
print(f'Minimum key is {list_keys[min_index]} and sentence is "{list_values[min_index]}"')