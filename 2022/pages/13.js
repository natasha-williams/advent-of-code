import React from 'react';

import { formatData, getTotal } from '@lib/utils';

import data from './api/13.txt';


class Packet {
    constructor (data, isDivider=false) {
        this.data = JSON.parse(data);
        this.isDivider = isDivider;
    }
}


class Packets {
    constructor (data, withDividerPackets=false) {
        this.data = data.map(item => formatData({ data: item }).map(line => new Packet(line)));

        if (withDividerPackets) {
            this.data.push(new Packet('[[2]]', true));
            this.data.push(new Packet('[[6]]', true));
        }
    }

    getComparison (left, right) {
        const isArrayLeft = Array.isArray(left);
        const isArrayRight = Array.isArray(right);

        if (!isArrayLeft && !isArrayRight) {
            return left - right;
        }

        if (!isArrayLeft) {
            left = [left];
        }

        if (!isArrayRight) {
            right = [right];
        }

        for (var index = 0; index < Math.min(left.length, right.length); index++) {
            const comparison = this.getComparison(left[index], right[index]);

            if (comparison !== 0) {
                return comparison;
            }
        }

        return left.length - right.length;
    }

    getCorrect () {
        return this.data.map((item, index) => this.getComparison(item[0].data, item[1].data) < 0 ? index + 1 : 0);
    }

    orderPackets () {
        return this.data.flat().sort((a, b) => this.getComparison(a.data, b.data))
            .map((item, index) => item.isDivider ? index + 1 : 0)
            .filter(item => item > 0)
            .reduce((sum, item) => sum * item);
    }
}


export default function Day13() {
    const formattedData = formatData({ data, splitAt: '\n\n' });

    const part1 = () => {
        const packets = new Packets(formattedData);
        return getTotal(packets.getCorrect());
    };

    const part2 = () => {
        const packets = new Packets(formattedData.join('\n').split('\n'), true);
        return packets.orderPackets();
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
