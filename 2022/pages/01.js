import React from 'react';

import { formatData, getTotal } from '@lib/utils';

import data from './api/01.txt';


export default function Day01() {
    const listData = formatData({ data, splitAt: '\n\n' });
    const formattedData = listData.map(item => formatData({ data: item, parseFn: parseInt }));
    const totals = formattedData.map(getTotal);
    totals.sort((a, b) => a - b);

    return (
        <React.Fragment>
            <section>
                <h1>Part 1</h1>
                <p>{totals[totals.length - 1]}</p>
            </section>

            <section>
                <h1>Part 2</h1>
                <p>{totals[totals.length - 1] + totals[totals.length - 2] + totals[totals.length - 3]}</p>
            </section>
        </React.Fragment>
    );
}
