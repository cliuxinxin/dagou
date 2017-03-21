@extends('layouts.app')

@section('content')
    <div class="container">
        <row>
            <h1>{{ $book->name }}</h1>
            <blockquote>
                《{{ $book->name }}》 的借阅记录
            </blockquote>
        </row>
        <hr>
        <div class="row">
            <table class="table table-striped">
                <tr>
                    <th>用户名</th>
                    <th>借阅开始</th>
                    <th>借阅结束</th>
                </tr>
                @foreach($items as $item)
                    <tr>
                        <td>{{$item->user->name}}</td>
                        <td>{{$item->start_at}}</td>
                        <td>{{$item->end_at}}</td>
                @endforeach
            </table>
        </div>
    {{ $items->links() }}
@endsection
