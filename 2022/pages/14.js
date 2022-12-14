import React from 'react';

import { formatData } from '@lib/utils';

import data from './api/14.txt';


class Coordinate {
    constructor (data) {
        const [x, y] = data.split(',');
        this.x = parseInt(x);
        this.y = parseInt(y);
        [this.initX, this.initY] = [this.x, this.y];
    }

    reset () {
        [this.x, this.y] = [this.initX, this.initY];
    }

    getCoordinates (coord) {
        const minX = Math.min(this.x, coord.x);
        const maxX = Math.max(this.x, coord.x);
        const minY = Math.min(this.y, coord.y);
        const maxY = Math.max(this.y, coord.y);
        const data = new Set();

        for (let y = minY; y <= maxY; y++) {
            for (let x = minX; x <= maxX; x++) {
                data.add(`${x},${y}`);
            }
        }

        return data;
    }

    moveDown () {
        this.y++;
    }

    moveLeft () {
        this.x--;
    }

    moveRight () {
        this.x++;
    }
}


class Cave {
    constructor (data, offset=0) {
        this.test = data;
        this.data = data.map(item => {
            const line = formatData({ data: item, splitAt: '->' });
            return [...Array(line.length - 1).keys()].map(index => {
                return [new Coordinate(line[index]), new Coordinate(line[index + 1])];
            });
        });
        this.blockers = this.getBlockers();
        this.offset = offset;
        this.maxY = Math.max(...this.blockers.map(item => item.y)) + offset;
        this.current = new Coordinate('500,0');
        this.sand = 0;
    }

    getBlockers () {
        let data = new Set();

        this.data.forEach(item => {
            item.forEach(coord => {
                coord[0].getCoordinates(coord[1]).forEach(item => data.add(item));
            });
        });

        return [...data].map(item => new Coordinate(item));
    }

    isDownBlocked () {
        return this.blockers.find(item => item.x === this.current.x && item.y === this.current.y + 1);
    }

    isDownLeftBlocked () {
        return this.blockers.find(item => item.x === this.current.x - 1 && item.y === this.current.y + 1);
    }

    isDownRightBlocked () {
        return this.blockers.find(item => item.x === this.current.x + 1 && item.y === this.current.y + 1);
    }

    isRest () {
        return this.blockers.find(item => item.x === 500 && item.y === 0);
    }

    addBlocker () {
        this.blockers.push(new Coordinate(`${this.current.x},${this.current.y}`));
        this.sand++;
    }

    hasFinished () {
        return (this.offset === 0 && this.current.y > this.maxY) || (this.offset !== 0 && this.isRest());
    }

    move () {
        while (true) {
            if (!this.isDownBlocked()) {
                this.current.moveDown();
            } else if (!this.isDownLeftBlocked()) {
                this.current.moveDown();
                this.current.moveLeft();
            } else if (!this.isDownRightBlocked()) {
                this.current.moveDown();
                this.current.moveRight();
            } else {
                break;
            }

            if (this.offset !== 0 && this.current.y === this.maxY - 1) {
                break;
            }

            if (this.hasFinished()) {
                break;
            }
        }
    }

    simulate () {
        while (!this.hasFinished()) {
            this.move();

            if (this.hasFinished()) {
                break;
            }

            this.addBlocker();
            this.current.reset();
        }

        return this.sand;
    }
}


export default function Day14() {
    const formattedData = formatData({ data });

    const part1 = () => {
        const cave = new Cave(formattedData, 0);
        return cave.simulate();
    };

    const part2 = () => {
        const cave = new Cave(formattedData, 2);
        return cave.simulate();
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
