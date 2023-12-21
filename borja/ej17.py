def create_tables(db_con, csv):
		cur = db_con.cursor()
		with open(csv, 'r') as f:
			for line in f:
				words = line.split(',')
				sql = 'CREATE TABLE ' + words[0] + ' ('
				for i in range(1, len(words)):
					sql += words[i].strip()
					if i < len(words) - 1:
						sql += ', '
				sql += ');'
				cur.execute(sql)
		db_con.commit()
		cur.close()
