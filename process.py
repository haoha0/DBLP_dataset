from dblp_parser import DBLP_Parser as dp

dblp = dp()

# dblp.download_latest_dump()

filename = 'dblp-2024-10-01.xml'

# execute the parser from the dblp class
parser, handler = dblp.execute_parser(filename=filename)

# you can use the handler to convert the handler output to dataframe
handler.to_df()

# the dataframe can be persisted as a pickle file or exported as csv file
handler.to_csv() # export to csv
handler.save() # persist as pickle