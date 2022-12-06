import React from 'react';

import { formatData } from '@lib/utils';

import data from './api/05.txt';


class Stacks {
    constructor (stacks, steps) {
        this.stacks = [...Array(stacks[0].length).keys()].map(num => new Stack(num, stacks));
        this.steps = steps;
    }

    process () {
        this.steps.forEach(([num, from, to]) => {
            [...Array(num).keys()].map(item => {
                this.stacks[to - 1].add(this.stacks[from - 1].delete(1));
            });
        });

        return this.stacks.map(item => item.stack[0]).join('');
    }

    processMultiple () {
        this.steps.forEach(([num, from, to]) => {
            this.stacks[to - 1].add(this.stacks[from - 1].delete(num));
        });

        return this.stacks.map(item => item.stack[0]).join('');
    }
}


class Stack {
    constructor (num, stacks) {
        const stack = stacks.map(item => item[num]);
        this.stack = stack.filter(item => item !== '');
    }

    add (item) {
        this.stack.unshift(...item);
    }

    delete (num) {
        return this.stack.splice(0, num); 
    }
}


export default function Day05() {
    const [dataStacks, dataSteps] = formatData({ data, splitAt: '\n\n' });
    const steps = formatData({ data: dataSteps }).map(item => item.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ')).map(item => {
        return formatData({ data: item, splitAt: ' ', parseFn: parseInt });
    });
    const stringStacks = dataStacks.split('    ').join(' ');
    const listStacks = formatData({ data: stringStacks }).map(item => item.split('[').join('').split(']').join('').split(' '));
    listStacks.pop();
    
    const part1 = () => {
        const stacks = new Stacks(listStacks, steps);
        return stacks.process();
    };

    const part2 = () => {
        const stacks = new Stacks(listStacks, steps);
        return stacks.processMultiple();
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
