import React from 'react';

import { formatData, getChunks, getTotal } from '@lib/utils';

import data from './api/03.txt';


class Rucksacks {
    constructor (items=[]) {
        this.firstRucksack = items[0];
        this.secondRucksack = items[1];
        this.thirdRucksack = items[2];
    }

    getDuplicate () {
        return this.firstRucksack.find(item => this.secondRucksack.includes(item) &&
            this.thirdRucksack.includes(item));
    }

    convertLetter () {
        const letter = this.getDuplicate();
        const offset = letter.toLowerCase() === letter ? 96 : 38;
        return letter.charCodeAt(0) - offset;
    }
}


class Rucksack extends Rucksacks {
    constructor (items) {
        super();
        this.firstCompartment = items.slice(0, items.length / 2);
        this.secondCompartment = items.slice(items.length / 2, items.length);
    }

    getDuplicate () {
        return this.firstCompartment.find(item => this.secondCompartment.includes(item));
    }
}


export default function Day03() {
    const listData = formatData({ data });
    const formattedData = listData.map(item => formatData({ data: item, splitAt: '' }));

    const part1 = () => {
        return getTotal(formattedData.map(item => new Rucksack(item).convertLetter()));
    };

    const part2 = () => {
        return getTotal(getChunks(formattedData, 3).map(item => new Rucksacks(item).convertLetter()));
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
