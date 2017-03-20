@extends('layouts.app')

@section('content')
    <div class="container">
        <row>
            <h1>共享图书馆</h1>
            <blockquote>
                大家可以把自己的书放上来共享。系统可以帮忙追踪书本的借阅情况。
            </blockquote>
        </row>
        <hr>
        <div class="row">
            <table class="table table-striped">
                <tr>
                    <th>书名</th>
                    <th>拥有者（微信号）</th>
                    <th>介绍</th>
                    <th>借阅</th>
                </tr>
                @foreach($items as $item)
                    <tr>
                        <td>{{$item->name}}</td>
                        <td>{{$item->user->profiles->first()->weixin}}</td>
                        <td>{{$item->detail}}</td>
                        <td>
                            <form method="POST" action="{{ route('lendingRecordStore',$item->id) }}">
                                {{ csrf_field() }}
                                <button type="submit" class="btn-sm btn-success">借阅</button>
                            </form>
                        </td>
                    </tr>
                @endforeach
            </table>
        </div>
        {{ $items->links() }}
        <hr>
        <div class="row col-md-6">
            <form method="POST" action="{{ route('bookStore') }}">
                {{ csrf_field() }}
                <div class="form-group">
                    <label for="name">书名</label>
                    <input type="text" class="form-control" name="name">
                </div>

                <div class="form-group" >
                    <label for="detail">介绍</label>
                    <textarea rows="3" class="form-control" name="detail"></textarea>
                </div>

                <button type="submit" class="btn btn-success">添加</button>
            </form>
        </div>
    </div>
@endsection
