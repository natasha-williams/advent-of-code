import React from 'react';

import { formatData } from '@lib/utils';

import data from './api/04.txt';


export default function Day04() {
    const listData = formatData({ data });
    const formattedData = listData.map(item => formatData({ data: item, splitAt: ',' })).map(item => {
        return [
            formatData({ data: item[0], splitAt: '-', parseFn: parseInt }),
            formatData({ data: item[1], splitAt: '-', parseFn: parseInt }),
        ];
    });

    const part1 = () => {
        return formattedData.filter(([a, b]) => (a[0] >= b[0] && a[1] <= b[1]) || (b[0] >= a[0] && b[1] <= a[1])).length;
    };

    const part2 = () => {
        return formattedData.filter(([a, b]) => {
            const aList = [...Array(a[1] - a[0] + 1).keys()].map(i => i + a[0]);
            const bList = [...Array(b[1] - b[0] + 1).keys()].map(i => i + b[0]);
            return aList.find(item => bList.includes(item)) !== undefined;
        }).length;
    };

    return (
        <React.Fragment>
            <section>
                <h1>Part 1</h1>
                <p>{part1()}</p>
            </section>

            <section>
                <h1>Part 2</h1>
                <p>{part2()}</p>
            </section>
        </React.Fragment>
    );
}
