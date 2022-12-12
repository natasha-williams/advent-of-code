import React from 'react';

import { formatData } from '@lib/utils';

import data from './api/11.txt';


class Monkey {
    constructor (monkey, start, operation, test, actionTrue, actionFalse) {
        const opData = operation.split(' ');
        const testData = test.split(' ');
        const trueData = actionTrue.split(' ');
        const falseData = actionFalse.split(' ');
        this.items = formatData({ 
            data: formatData({ data: start, splitAt: ':' })[1], 
            splitAt: ',', parseFn: parseInt, 
        });
        this.operation = opData[opData.length - 2];
        this.number = parseInt(opData[opData.length - 1])
        this.test = parseInt(testData[testData.length - 1]);
        this.numTrue = parseInt(trueData[trueData.length - 1]);
        this.numFalse = parseInt(falseData[falseData.length - 1])
        this.count = 0;
    }

    play (data, divideNum, remainNum) {
        while (this.items.length > 0) {
            this.count++;
            let item = this.getNumber(this.items.shift());

            if (divideNum > 0) {
                item = Math.floor(item / divideNum);
            }

            if (remainNum > 0) {
                item %= remainNum;
            }

            data[item % this.test === 0 ? this.numTrue : this.numFalse].items.push(item);
        }
    }

    getNumber (currentNumber) {
        const number = isNaN(this.number) ? currentNumber : this.number;

        switch (this.operation) {
            case '*':
                return currentNumber * number;
            case '+':
                return currentNumber + number;
        }
    }
}


class Game {
    constructor (data) {
        this.data = data.map(item => new Monkey(...formatData({ data: item })));
    }

    getHighest () {
        return this.data.reduce((sum, next) => sum *= next.test, 1);
    }

    run (rounds, divideNum, remainNum) {
        while (rounds != 0) {
            this.data.forEach(item => {
                item.play(this.data, divideNum, remainNum);
            });

            rounds--;
        }

        const inspections = this.data.map(item => item.count);
        inspections.sort((a, b) => b - a);
        return inspections[0] * inspections[1];
    }
}


export default function Day11() {
    const part1 = () => {
        const game = new Game(formatData({ data, splitAt: '\n\n' }));
        return game.run(20, 3, 0);
    };

    const part2 = () => {
        const game = new Game(formatData({ data, splitAt: '\n\n' }));
        return game.run(10000, 0, game.getHighest());
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
