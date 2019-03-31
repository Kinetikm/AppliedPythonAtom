#!/usr/bin/env python
# coding: utf-8

import csv

def outputData(data, filename):
    with open(file=filename, mode='w', newline='') as f:
        fnames = ['link', 'username', 'count_comment']
        writer = csv.DictWriter(f, delimiter=',', fieldnames=fnames)

        writer.writeheader()
        for link_data in data.items():
            for ccomments_usernames in link_data[1].items():
                for username in ccomments_usernames[1]:
                    writer.writerow({fnames[0]: link_data[0],
                                     fnames[1]: username,
                                     fnames[2]: ccomments_usernames[0]})
