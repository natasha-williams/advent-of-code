import React from 'react';

import { formatData, getTotal } from '@lib/utils';

import data from './api/02.txt';

const SCORE_MAP = {
    X: 'A',
    Y: 'B',
    Z: 'C',
};


class Round {
    LOSE_SCORE = 0
    DRAW_SCORE = 3
    WIN_SCORE = 6
    SCORES = {
        A: 1,
        B: 2,
        C: 3,
    }

    constructor (otherScore, myScore) {
        this.otherScore = this.SCORES[otherScore];

        if (myScore === 'X') {
            this.myScore = this.getLosing();
        } else if (myScore === 'Y') {
            this.myScore = this.otherScore;
        } else if (myScore === 'Z') {
            this.myScore = this.getWinning();
        } else {
            this.myScore = this.SCORES[myScore];
        }
    }

    getWinning () {
        const scores = [...Object.values(this.SCORES)];
        const score = this.otherScore + 1;
        return scores.includes(score) ? score : Math.min(...scores);
    }

    getLosing () {
        const scores = [...Object.values(this.SCORES)];
        return scores.find(item => item !== this.otherScore && item !== this.getWinning());
    }

    isWinner () {
        return this.getWinning() === this.myScore;
    }

    isLoser () {
        return this.getLosing() === this.myScore;
    }

    getScore () {
        if (this.myScore === this.otherScore) {
            return this.DRAW_SCORE + this.myScore;
        } else if (this.isWinner()) {
            return this.WIN_SCORE + this.myScore;
        } else if (this.isLoser()) {
            return this.LOSE_SCORE + this.myScore;
        }
    }
}


export default function Day02() {
    const listData = formatData({ data });
    const formattedData = listData.map(item => formatData({ data: item, splitAt: ' ' }));

    const part1 = () => {
        return getTotal(formattedData.map(([a, b]) => new Round(a, SCORE_MAP[b]).getScore()));
    };

    const part2 = () => {
        return getTotal(formattedData.map(([a, b]) => new Round(a, b).getScore()));
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
