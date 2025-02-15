input_args_list = ['model_state', 'my_db_state', 'selection_docs_state', 'requests_state']

no_default_param_names = [
    'instruction',
    'iinput',
    'context',
    'instruction_nochat',
    'iinput_nochat',
]

gen_hyper = ['temperature',
             'top_p',
             'top_k',
             'num_beams',
             'max_new_tokens',
             'min_new_tokens',
             'early_stopping',
             'max_time',
             'repetition_penalty',
             'num_return_sequences',
             'do_sample',
             ]

reader_names = ['image_loaders', 'pdf_loaders', 'url_loaders', 'jq_schema']

eval_func_param_names = ['instruction',
                         'iinput',
                         'context',
                         'stream_output',
                         'prompt_type',
                         'prompt_dict'] + \
                        gen_hyper + \
                        ['chat',
                         'instruction_nochat',
                         'iinput_nochat',
                         'langchain_mode',
                         'add_chat_history_to_context',
                         'langchain_action',
                         'langchain_agents',
                         'top_k_docs',
                         'chunk',
                         'chunk_size',
                         'document_subset',
                         'document_choice',
                         'pre_prompt_query',
                         'prompt_query',
                         'pre_prompt_summary',
                         'prompt_summary',
                         'system_prompt',
                         ] + \
                        reader_names

# form evaluate defaults for submit_nochat_api
eval_func_param_names_defaults = eval_func_param_names.copy()
for k in no_default_param_names:
    if k in eval_func_param_names_defaults:
        eval_func_param_names_defaults.remove(k)

eval_extra_columns = ['prompt', 'response', 'score']
