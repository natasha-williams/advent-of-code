import React from 'react';

import { formatData, getTotal } from '@lib/utils';

import data from './api/08.txt';


class Tree {
    constructor (row, column, height) {
        this.row = row;
        this.column = column;
        this.height = parseInt(height);
    }

    isEdge (maxRow, maxColumn) {
        return this.row === 0 || this.column === 0 ||
            this.row === maxRow - 1 || this.column === maxColumn - 1;
    }

    isValid (tree) {
        return tree.height < this.height;
    }

    getDirections (trees) {
        const rows = trees[this.row];
        const columns = trees[this.row].map((tree, index) => trees[index][this.column]);

        return [
            [...rows.slice(0, this.column)].reverse(), // Left
            rows.slice(this.column + 1), // Right
            [...columns.slice(0, this.row)].reverse(), // Top
            columns.slice(this.row + 1), // Bottom
        ];
    }

    isVisible (trees) {
        return this.getDirections(trees).map(x => x.every(tree => this.isValid(tree))).some(Boolean);
    }

    getScenicScore (trees, maxRow, maxColumn) {
        const directions = this.getDirections(trees).map(item => item.map(tree => {
            return this.isValid(tree) || tree.isEdge(maxRow, maxColumn); 
        }));
        const scores = directions.map(item => {
            return item.indexOf(false) === -1 ? item.length : item.indexOf(false) + 1;
        });
        return scores.reduce((sum, next) => sum * next, 1);
    }
}


class Forest {
    constructor (data) {
        this.data = data.map((item, row) => item.split('').map((num, col) => {
            return new Tree(row, col, num);
        }));
        this.numRows = this.data.length;
        this.numColumns = this.data[0].length;
    }

    getVisible () {
        return this.data.map(row => {
            return row.map(tree => {
                return tree.isEdge(this.numRows, this.numColumns) || tree.isVisible(this.data);
            });
        }).flat();
    }

    getViewingDistances () {
        return this.data.map(row => {
            return row.map(tree => {
                return tree.getScenicScore(this.data, this.numRows, this.numColumns);
            });
        }).flat();
    }
}


export default function Day08() {
    const trees = new Forest(formatData({ data }));
    
    const part1 = () => {
        return getTotal(trees.getVisible());
    };

    const part2 = () => {
        return Math.max(...trees.getViewingDistances());
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
